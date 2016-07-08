#!/usr/bin/env python
#coding:utf-8
import os
import urllib
import requests
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "puppet.settings")
import django
django.setup()


def nodes_get():
    from osweb.models import Online,Offline
    params = {'query':'["extract", ["certname"]]'}
    data = urllib.urlencode(params)
    url = 'http://localhost:8080/pdb/query/v4/nodes'
    nodes = requests.get(url,params=data)
    nodename = []
    for node in nodes.json():
        nodename.append(node['certname'].rstrip('.boss'))
    online_host = []
    for i in os.popen('/opt/puppetlabs/bin/mco find').readlines():
        online_host.append(i.strip('\n').rstrip('.boss').lower())
    total = set(nodename)
    online = set(online_host)
    offline = total - online
    Online.objects.all().delete()
    Offline.objects.all().delete()
    for on in online_host:
      Online.objects.create(online=on)
    for off in list(offline):
      Offline.objects.create(offline=off) 

if __name__ == '__main__':
     nodes_get()
