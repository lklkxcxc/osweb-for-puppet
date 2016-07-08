from django.db import models
from osweb.models import *
# Create your models here.
class Node(models.Model):
    node_name = models.CharField(max_length=30, primary_key=True)
    cpu = models.CharField(max_length=80,null=True)
    mem = models.CharField(max_length=80,null=True)
    ip = models.GenericIPAddressField(null=True)
    netmask = models.GenericIPAddressField(null=True)
    gateway = models.GenericIPAddressField(null=True)
    os_release = models.CharField(max_length=80,null=True)
    pesize = models.CharField(max_length=300,null=True)
    lang = models.CharField(max_length=80,null=True)
    keyboard = models.CharField(max_length=80,null=True)
    timezone = models.CharField(max_length=100,null=True)
    ntp = models.CharField(max_length=300,null=True)
    password = models.CharField(max_length=100,null=True)
    swap = models.CharField(max_length=100,null=True)
    filesystem = models.CharField(max_length=2400,null=True)
    boot = models.CharField(max_length=100,null=True)
    software = models.CharField(max_length=80,null=True)
    security = models.CharField(max_length=100,null=True)
    toptea = models.CharField(max_length=80,null=True)
    init = models.CharField(max_length=100,null=True)
    network_speed = models.CharField(max_length=120,null=True)
    bond_mode = models.CharField(max_length=600,null=True)
    tmout = models.CharField(max_length=100,null=True)
    ulimit = models.CharField(max_length=100,null=True)
    app = models.CharField(max_length=200,null=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.node_name


class Modules(models.Model):
      module_name = models.CharField(max_length=200)
      env = models.CharField(max_length=200,null=False)
      def __unicode__(self):              # __unicode__ on Python 2
        return self.module_name

class Classes(models.Model):
      node_name = models.ForeignKey(Node)
      class_name = models.CharField(max_length=100)
      class_env = models.CharField(max_length=200)
      def __unicode__(self):              # __unicode__ on Python 2
        return self.node_name_id
       


class Report(models.Model):
      node_name = models.ForeignKey(Node)
      class_name = models.CharField(max_length=200,null=True)
      end_time = models.DateTimeField(max_length=200,null=True)
      status = models.CharField(max_length=200,null=True)

class Online(models.Model):
      online = models.CharField(max_length=200)

class Offline(models.Model):
      offline = models.CharField(max_length=200)

