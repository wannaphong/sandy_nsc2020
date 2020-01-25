#!/usr/bin/env python3

import pyaudio
import socket

ADDRESS = ('localhost', 10000)
CHUNK_SIZE = 2048

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ADDRESS)

audio = pyaudio.PyAudio()
stream = audio.open(
    format=pyaudio.paInt16, channels=1,
    rate=16000, input=True, frames_per_buffer=CHUNK_SIZE
)

try:
    while True:
        sock.sendall(stream.read(CHUNK_SIZE))
finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()
    sock.close()
