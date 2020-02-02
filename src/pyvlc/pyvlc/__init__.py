# -*- coding: utf-8 -*-
import subprocess

def playfile(file):
    subprocess.Popen(['vlc','--one-instance',file], shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)

def quitfile():
    subprocess.Popen(['vlc','--one-instance','vlc://quit'], shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)