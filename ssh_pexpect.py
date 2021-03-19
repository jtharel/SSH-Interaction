#!/usr/bin/python3

import pexpect

cmd = pexpect.spawn('ssh pooneth@1.1.1.1')
#cmd to run

cmd.expect_exact('Password:')

cmd.sendline('password')
#password to send

cmd.expect_exact('pooneth@MacBook-Pro ~ %')
#command prompt that is returned

cmd.sendline('cat /etc/hosts')
cmd.expect_exact('pooneth@MacBook-Pro ~ %')

for line in cmd.before.split(b'\n'):
    print(line)


