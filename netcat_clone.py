#!/bin/python3

import os
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
    filename = os.path.basename(__file__)
    print('########################################################')
    print('#                                                      #')
    print('#                    [ BHP net tool ]                  #')
    print('#                                                      #')
    print('########################################################')
    print('\n')
    print('Usage: ./{} -t <target_ip> -p <port>'.format(filename))
    print('-l   --listen                    - listen on [host]:[port] for incoming connections')
    print('-e   --execute=<file_to_run>     - execute the given file upon receiving a connection')
    print('-c   --command                   - initialize command shell')
    print('-u   -- upload=<destination>     - upon receiving a connection, upload a file and write to <destination>')
    print('\n\n')
    print('Examples:')
    print('./{} -t 192.168.0.1 -p 5555 -l -c'.format(filename))
    print('./{} -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe'.format(filename))
    print('./{} -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"'.format(filename))
    print('./{} -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe'.format(filename))
    print('echo \'ABCDEFGHI\' | ./{} -t 192.168.11.12 -p 135'.format(filename))
    sys.exit(0)

def main():
    global listen
    global command
    global upload
    global execute
    global target
    global upload_destination
    
    if not len(sys.argv[1:]):
        usage()

main()