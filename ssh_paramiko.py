#!/usr/bin/python3

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('1.1.1.1', username='pooneth', password='password')

stdin, stdout, stderr = ssh.exec_command('cat /etc/hosts')

for line in stdout.readlines():
        print (line.strip())

ssh.close()

