import nmap # type: ignore
from src.help import *
import datetime
import subprocess

class NmapProject:
    def __init__(self, arguments, target):
        self.nmap = nmap.PortScanner()
        self.arguments = arguments
        self.target = target
        self.argumentsPort()

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

    def argumentsPort(self):
        now = datetime.datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        getArgument = self.arguments[2:]
        if len(getArgument) < 1:
            Help.exampleUsageForNmap()
        elif len(getArgument) >= 1:
            try:
                target = self.arguments[-1] 
                print("Starting pinfo v1.0 ( https://nextjiesdev.site ) at", formatted_time)
                print("pinfo scan report for target =>", target)
                arguments = getArgument[:-1]
                resultArguments = ' '.join(str(e) for e in arguments)
                port = None
                sudo = False
                for i in getArgument:
                    if i == "-O":
                        sudo = True
                    else:
                        sudo = False

                if self.ping_host(host=target):
                    self.nmap.scan(hosts=target, ports=port, sudo=sudo, arguments=resultArguments)
                    # print(self.nmap.all_hosts())
                    service_versions = {}
                    for host in self.nmap.all_hosts():
                        print(f"Host is {self.nmap[host].state()}")
                        for proto in self.nmap[host].all_protocols():
                            print("Protocol: ", proto)
                            ports = self.nmap[host][proto].keys()
                            service_info = self.nmap[host][proto][port]
                            service_versions[port] = service_info['service']['version']
                            for port in ports:
                                print("Port: ", port, "State: ", self.nmap[host][proto][port]['state'])
            except Exception as e:
                print(e)
        else:
            print("Error")     