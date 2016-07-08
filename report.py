#!/usr/bin/python
#coding=utf-8
import os
import urllib
import requests
import json
import getopt
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "puppet.settings")
import django
django.setup()

def reports(hostname,classes=None):
    if classes is not None and hostname is not None:
       classes = classes.capitalize()
       params = {'query':'["extract",["status","run_end_time","containing_class","certname"], \
       ["and",["=","certname","'+hostname+'"],["~","containing_class","'+classes+'"]]]'}
    else:
       params = {'query':'["extract",["status","run_end_time","containing_class","certname"], \
       ["=","certname","'+hostname+'"]]'}      

    data = urllib.urlencode(params)
    url = 'http://localhost:8080/pdb/query/v4/events'
    events = requests.get(url,params=data)

    classes_list = []
    for item in events.json():
        classes_list.append(item['containing_class'])
    c = {}
    for classes in classes_list:
        c[classes] = []
        for item in events.json():
            if classes == item['containing_class']:
               c[classes].append(item)
    report = []
    for i in c:
        di = max(c[i], key=lambda x:x["run_end_time"])
        report.append(di)
    return report

def imp_report():
    from osweb.models import Node,Report
    node_names = Node.objects.all().values('node_name')
    for node in node_names:
        report = reports(node['node_name'])
        if report is not None:
           for i in report:
             Report.objects.get_or_create(node_name_id=i['certname'],end_time=i['run_end_time'],defaults={'class_name':i['containing_class'],'status':i['status']})


if __name__ == '__main__':
     imp_report()
