#coding:utf-8
import os
from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from osweb.models import *
from django.db import connection, transaction
from django.template.defaulttags import register
from django.contrib import auth
from django.template import RequestContext
import json
import paramiko
import re
import ssh
from django.views.generic.list import ListView
import time

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def index(request):
    user = request.user
    node_general =  Node.objects.all().values("node_name","cpu","mem","ip","app")
    last_time = {}
    cursor = connection.cursor()
    for node in node_general:
      cursor.execute("select end_time from osweb_report where node_name_id='"+node['node_name']+"' order by end_time desc limit 1")
      end_time = cursor.fetchone()
      last_time[node['node_name']] = end_time[0]
    cursor.close()
    online = len(Online.objects.all())
    offline = len(Offline.objects.all())
    return render_to_response('index.html',{'node_general':node_general,'last_time':last_time,'user':user,'online':online,'offline':offline})


def nodes(request,nodename):
    node_name = Node.objects.filter(node_name=nodename)
    return render_to_response('nodes.html',{'node_name':node_name})


     
def config(request):
    user = request.user
    if request.user.is_authenticated():
       authuser = "pass"
    else:
       authuser = "failed"
    cursor = connection.cursor()
    cursor.execute('select distinct app from osweb_node')
    env = cursor.fetchall()
    nodes = {}
    for e in env:
      for n in Node.objects.filter(app=e[0]):
        nodes.setdefault(e[0],[]).append(n.node_name)
    cursor.execute('select distinct env from osweb_modules')
    envs = cursor.fetchall()
    modules = {}
    for es in envs:
      for m in Modules.objects.filter(env=es[0]):
        modules.setdefault(es[0],[]).append(m.module_name)
    error = ''
    if request.method == 'POST':
        if request.POST.has_key('delete'):
          node_name = request.POST.getlist('node_name')
          class_names = request.POST.getlist('class_name')
          if len(node_name) !=0 and len(class_names) !=0:
             for node in node_name:
               apps = Node.objects.get(node_name=node)
               for module_names in class_names:
                 try:
                   Classes.objects.get(class_name=module_names,node_name_id=node,class_env=apps.app).delete()
                 except:
                   error = '请检查，该主机未配置该类名！'
             os.popen('python /root/puppet/node.pyc')
          else:
           error = '未选择主机名或者类名!' 
        else:
          node_name = request.POST.getlist('node_name')
          class_names = request.POST.getlist('class_name')
          if len(node_name) !=0 and len(class_names) !=0:
             for node in node_name:
               apps = Node.objects.get(node_name=node)
               for module_names in class_names:
                 Classes.objects.update_or_create(class_name=module_names,node_name_id=node,class_env=apps.app)
             os.popen('python /root/puppet/node.pyc')
          else:
           error = '未选择主机名或者类名!'
    envent = {}
    class_name = {}
    for nodename in Node.objects.all().values('node_name'):
        app = Node.objects.get(node_name=nodename['node_name'])
        envent[app.node_name] = app.app
        for classname in Classes.objects.filter(node_name_id=app.node_name):
            class_name.setdefault(app.node_name,[]).append(classname.class_name)
    return render_to_response('config.html',{"nodes":nodes,"modules":modules,"error":error,'class_name':class_name,'envent':envent,'user':user,'authuser':authuser})

def report(request):
    user = request.user
    report = Report.objects.all()
    return render_to_response('report.html',{'report':report,'user':user})

def run(request):
    user = request.user
    if request.user.is_authenticated():
       authuser = "pass"
    else:
       authuser = "failed"
    cursor = connection.cursor()
    cursor.execute('select distinct app from osweb_node')
    env = cursor.fetchall()
    nodes = {}
    for e in env:
      for n in Node.objects.filter(app=e[0]):
        nodes.setdefault(e[0],[]).append(n.node_name)
    report = ''
    error = ''
    if request.method == 'POST':
        opts = request.POST.getlist('node_name')
        if len(opts) !=0:
           report = os.popen('python /root/puppet/run.pyc '+','.join(opts)).readlines()
        else:
           error = '未选择主机列表！'
    return render_to_response('run.html',{'nodes':nodes,'report':report,'error':error,'user':user,'authuser':authuser})


def login(request):
    error = ''
    if request.method == 'GET':
       request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
    elif request.method == 'POST':
       if request.POST.has_key('username') and request.POST.has_key('password'):
          username = request.POST.get('username')
          password = request.POST.get('password')
          user = auth.authenticate(username=username,password=password)
          if user is not None:
             auth.login(request,user)
             return HttpResponseRedirect(request.session['login_from'])
          else:
             error = '用户或者密码错误！'
       else:
          error = '请输入用户名或密码！'
    return render_to_response('login.html',{'error':error})

def logout(request):
      user = request.user
      auth.logout(request)
      return render_to_response("logout.html",{'user':user})

def dashboard(request):
    user = request.user
    node_general =  Node.objects.all().values("node_name","cpu","mem","ip","app")
    last_time = {}
    cursor = connection.cursor()
    for node in node_general:
      cursor.execute("select end_time from osweb_report where node_name_id='"+node['node_name']+"' order by end_time desc limit 1")
      end_time = cursor.fetchone()
      last_time[node['node_name']] = end_time[0]
    cursor.close()
    return render_to_response('dashboard.html',{'user':user,'node_general':node_general,'last_time':last_time})


def export(request):
    user = request.user
    return render_to_response('export.html',{'user':user})

def status(request):
    user = request.user
    online = Online.objects.all()
    online_list = []
    for i in online:
        online_list.append(i.online)
    offline = Offline.objects.all()
    if request.method == 'POST':
       agent = request.POST.getlist('nodestatus')
       offline_list = set(agent) - set(online_list)
       for offhost in list(offline_list):
         try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(offhost,timeout=5)
            stdin, stdout, stderr = client.exec_command('service ntpd stop;ntpdate 10.168.25.101;service ntpd start')
            stdout.read()
            stdin, stdout, stderr = client.exec_command('service mcollective restart')
            stdout.read()
            print stderr.readlines()
            client.close()
         except:
            print offhost+" ssh error!"
       online_hosts = []
       for i in os.popen('mco find').readlines():
         online_hosts.append(i.strip('\n').lower())
       on_host = set(online_hosts) - set(online_list)
       for on in list(on_host):
         Online.objects.create(online=on)
         if Offline.objects.get(offline=on):
            Offline.objects.get(offline=on).delete()
       off_host = list(offline_list - on_host)
       return render_to_response('status.html',{"online":online,"offline":offline,'off_host':off_host,"user":user})
    else:
       return render_to_response('status.html',{"online":online,"offline":offline,"user":user})

def remote(request):
    user = request.user
    return render_to_response('remote.html',{"user":user})

def vnc_auto(request):
    return render_to_response('vnc_auto.html')

