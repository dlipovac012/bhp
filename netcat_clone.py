#/bin/python3

import sys
import socket
import getopt
import threading
import subprocess

# Globals
listen                  = False
command                 = False
upload                  = False
execute                 = ''
target                  = ''
upload_destination      = ''
port                    = 0

def usage():
    print('-=-=-=-= BHP net tool =-=-=-=-')
    print('\n')
    print('Usage: python3 netcat_clone.py -t <target_ip> -p <port>')
    print('-l   --listen                    - listen on [host]:[port] for incoming connections')
    print('-e   --execute=<file_to_run>     - execute the given file upon receiving a connection')
    print('-c   --command                   - initialize command shell')
    print('-u   -- upload=<destination>     - upon receiving a connection, upload a file and write to <destination>')
    print('\n\n')
    print('Examples:')
    print('./netcat_clone.py -t 192.168.0.1 -p 5555 -l -c')
    print('./netcat_clone.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe')
    print('./netcat_clone.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"')
    print('./netcat_clone.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe')
    print('echo \'ABCDEFGHI\' | ./bhpnet.py -t 192.168.11.12 -p 135')