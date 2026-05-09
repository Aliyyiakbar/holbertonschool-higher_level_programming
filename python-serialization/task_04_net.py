#!/usr/bin/env python3
"""Create a small client-server app using JSON serialization."""

import json
import socket


HOST = "127.0.0.1"
PORT = 65432


def start_server():
    """Start a server, receive JSON data, and print the dictionary."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((HOST, PORT))
            server.listen(1)

            connection, address = server.accept()

            with connection:
                data = b""

                while True:
                    chunk = connection.recv(1024)
                    if not chunk:
                        break
                    data += chunk

                received_dict = json.loads(data.decode("utf-8"))

                print("Received Dictionary from Client:")
                print(received_dict)

    except Exception as error:
        print("Server error: {}".format(error))


def send_data(data):
    """Serialize a dictionary and send it to the server."""
    try:
        serialized_data = json.dumps(data).encode("utf-8")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))
            client.sendall(serialized_data)

    except Exception as error:
        print("Client error: {}".format(error))
