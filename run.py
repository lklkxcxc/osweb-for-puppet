#!/usr/bin/env python
#coding:utf-8
import os,sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "puppet.settings")
import django
django.setup()

def run_job(name):
    runlist = ''
    for n in name.split(','):
        runlist += ' -I'+' '+n.rstrip('.boss')
    
    run_result = os.popen('/opt/puppetlabs/bin/mco puppet -v runonce'+runlist).readlines()
    for line in run_result:
       print line


if __name__ == '__main__':
     run_job(sys.argv[1])
