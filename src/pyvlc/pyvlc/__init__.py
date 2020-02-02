# -*- coding: utf-8 -*-
import subprocess
import os
def playfile(file):
    global v
    if os.name == 'nt':
        v=subprocess.Popen(['vlc',file], shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    else:
        v=subprocess.Popen(['cvlc',file], shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    return v
def quitfile():
    global v
    v.kill()
    #if os.name == 'nt':
    #    subprocess.Popen(['vlc','--one-instance','vlc://quit'], shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)
    #else:
    #    subprocess.Popen(['cvlc','--one-instance','vlc://quit'], shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)