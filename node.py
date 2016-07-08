#!/usr/bin/python
#coding=utf-8

import os
import sys
import yaml
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "puppet.settings")
import django
django.setup()

def addWord(d,key,value): 
    d.setdefault(key, [ ]).append(value)

def create_yaml():
    from osweb.models import Classes
    node_name = Classes.objects.all().values('node_name_id','class_env')
    for name in node_name:
        classes_name = Classes.objects.filter(node_name_id=name['node_name_id'])
        d = {}
        for peizhi in classes_name:
            addWord(d,'classes',str(peizhi.class_name))
        f = open('/etc/puppetlabs/code/environments/'+name['class_env']+'/hieradata/nodes/'+name['node_name_id'].lower()+'.yaml','w')
        yaml.dump(d,f)
        f.close

if __name__ == '__main__':
        create_yaml()
