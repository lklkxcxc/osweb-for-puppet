#!/usr/bin/env python
import paramiko
import re

class remote():
  def __init__(self,ip):
     self.ip = ip
     self.client = paramiko.SSHClient()
     self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     self.client.connect(self.ip, username='root', password='lk130130')
     self.shell = self.client.invoke_shell(term='vt100')
     

  def cmd(self,cmd):
      self.shell.send(cmd+'\n')
      recv_buffer = ''
      while not re.findall("]#(?!\s"+cmd+")",recv_buffer):
        recv_buffer += self.shell.recv(8192)
      return recv_buffer

  def close(self):
      self.client.close()
