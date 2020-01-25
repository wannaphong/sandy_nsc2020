#!/usr/bin/env python3

import socket
import  threading
from threading import Thread
#threading.TIMEOUT_MAX = 4294967.0
#threading.TIMEOUT_MAX = 4294967.0

from precise.network_runner import Listener
from precise_runner import PreciseRunner, ReadWriteStream, PreciseEngine
from precise_runner.runner import ListenerEngine

ADDRESS = ('localhost', 10000)
MODEL_NAME = 'jao-sandy.pb'
CHUNK_SIZE = 2048

stream = ReadWriteStream()
runner = PreciseRunner(
    PreciseEngine('precise-engine', MODEL_NAME),
    stream=stream, on_activation=lambda: print('Activated!')
)
runner.start()


class PreciseConnection:
    """Represents a socket connection routed to a precise process"""

    def __init__(self, connection, address):
        self.address = address
        self.connection = connection  # type: socket.socket
        self.stream = ReadWriteStream()
        self.runner = PreciseRunner(
            ListenerEngine(Listener(MODEL_NAME, CHUNK_SIZE), CHUNK_SIZE),
            1, stream=self.stream, on_activation=self.on_activation,
            on_prediction=self.on_prediction
        )
        self.runner.start()

    def on_activation(self):
        print(' --- ACTIVATION from:', self.address, '--- ')

    def on_prediction(self, conf):
        print('!' if conf > 0.5 else '.', end='', flush=True)

    def update(self):
        """Return whether connection still alive"""
        data = self.connection.recv(CHUNK_SIZE)
        self.stream.write(data)
        return bool(data)

    def close(self):
        print('Closing connection from', self.address)
        self.runner.stop()
        self.connection.close()


class ConnectionManager:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(ADDRESS)
        self.sock.listen(1)

        self.connections = []

    def wait_for_connection(self):
        print('Waiting for a connection...')
        connection, client_address = self.sock.accept()

        print('New connection:', client_address)
        self.connections.append(PreciseConnection(connection, client_address))

        Thread(target=self.wait_for_connection, daemon=True).start()

    def update(self):
        for i, conn in enumerate(list(self.connections)):
            if not conn.update():
                conn.close()
                del self.connections[i]

    def close(self):
        for i in self.connections:
            i.close()


def main():
    manager = ConnectionManager()
    manager.wait_for_connection()

    try:
        while True:
            manager.update()
    finally:
        manager.close()


if __name__ == '__main__':
    main()
