#!/usr/bin/python3
# scp commands to copy files to and from ssh server.

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('192.168.1.251', username='jtharel', password='Fluffkin101!')

scp = ssh.open_sftp()

scp.put('zip.txt', 'zipcode.txt')
#send file to scp server
#first file is the source file name the second is the destination file name you want

print(scp.listdir())

scp.chdir('/var/log')
scp.get('apache.log')


ssh.close()

