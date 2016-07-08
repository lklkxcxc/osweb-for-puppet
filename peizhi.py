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
    params = {'query':'["extract", ["certname"]]'}
    data = urllib.urlencode(params)
    url = 'http://localhost:8080/pdb/query/v4/nodes'
    nodes = requests.get(url,params=data)
    nodename = []
    for node in nodes.json():
        nodename.append(node['certname'])

    return nodename

def fact_get(hostname,fact,option=None):
  hostname = hostname.lower()
  params = {'query':'["and",["=","certname","'+hostname+'"],["=","name","'+fact+'"]]'}
  data = urllib.urlencode(params)
  url = 'http://localhost:8080/pdb/query/v4/facts'
  facts = requests.get(url,params=data)
  if len(facts.json()):
     if option is not None:
        try:
           if facts.json()[0]['value'].has_key(option):
              return facts.json()[0]['value'][option]
           else:
            return facts.json()[0]['value']
        except:
           return facts.json()[0]['value']
     else:
        return facts.json()[0]['value']
  else:
     return None

def imp_db():
    from osweb.models import Node
    for name in nodes_get():
       hostname = fact_get(name,'fqdn')
       cpu = unicode(fact_get(name,'processors','count'))
       mem = fact_get(name,'memory','system')['total']
       ip = fact_get(name,'ipaddress')
       netmask = fact_get(name,'netmask')
       gateway = fact_get(name,'router')
       if fact_get(name,'os','distro').has_key('description'):
          release = fact_get(name,'os','distro')['description']
       else:
          release = fact_get(name,'os','distro')
       vgs = fact_get(name,'vgs')
       lang = fact_get(name,'lang')
       keyboard = fact_get(name,'keyboard')
       tz = fact_get(name,'timezone')
       ntp = fact_get(name,'ntp')
       password = fact_get(name,'password')
       swap = fact_get(name,'swapsize')
       fs = fact_get(name,'mountpoints')
       if fact_get(name,'mountpoints','/boot') is not None:  
          if fact_get(name,'mountpoints','/boot').has_key('size'):
             boot = fact_get(name,'mountpoints','/boot')['size']
          else:
             boot = fact_get(name,'mountpoints','/boot')
       software = fact_get(name,'soft_groups')
       security = fact_get(name,'security')
       toptea = fact_get(name,'toptea')
       inittab = fact_get(name,'inittab')
       network = fact_get(name,'networking_speed')
       bond = fact_get(name,'bond')
       tmout = fact_get(name,'tmout')
       ulimit = fact_get(name,'ulimit')
       app = fact_get(name,'environment')

       Node.objects.update_or_create(node_name__exact=hostname,defaults={'node_name':hostname,'ip':ip,'cpu':cpu,'mem':mem,'netmask':netmask, \
                                    'gateway':gateway,'os_release':release,'pesize':vgs,'lang':lang,'keyboard':keyboard,'timezone':tz,'ntp':ntp, \
                                    'password':password,'swap':swap,'filesystem':fs,'boot':boot,'software':software,'security':security,'toptea':toptea, \
                                    'init':inittab,'network_speed':network,'bond_mode':bond,'tmout':tmout,'ulimit':ulimit,'app':app})

 
if __name__ == "__main__":
     imp_db()
