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
    print('-=-=-=-= BHP net tool =-=-=-=-\n')
    print('Usage: python3 netcat_clone.py -t <target_ip> -p <port>')
    print('-l --listen      - listen on [host]:[port] for incoming connections')