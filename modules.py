#!/usr/bin/env python
#coding:utf-8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "puppet.settings")
import django
django.setup()

def imp_module():
    from osweb.models import Modules
    envs = os.listdir('/etc/puppetlabs/code/environments')
    for env in envs:
        dir_modules = os.listdir('/etc/puppetlabs/code/environments/'+env+'/modules/')
        for module in dir_modules:
            Modules.objects.get_or_create(module_name=module,env=env)

        data_module = Modules.objects.filter(env=env)
        for module_d in data_module:
            if module_d.module_name not in dir_modules:
               module_d.delete()

if __name__ == '__main__':
     imp_module()
