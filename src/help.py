from colorama import Fore, Back, Style

class Help:
    @staticmethod
    def exampleUsage():
       print( """
EXAMPLES for Network Information Gathering:
./pinfo -n https://nextjiesdev.site
./pinfo -n -A --port 80 192.168.0.0/16
./pinfo -n -iR 10000 -Pn -p 80
        
EXAMPLES for DDoS Attack:
./pinfo -d -uD -t 10000 -p 80 -s 60 192.168.0.0/16
[-uD] UDP Method
[-tC] TCP Method
[-t] Thread Count (default 10)
[-p] Port of target (default 80)
[-s] Duration in second (default 60s)
""")
       
    @staticmethod
    def exampleUsageForNmap():
        print("""
EXAMPLES for Network Information Gathering:
pinfo -n https://nextjiesdev.site
pinfo -n -A --port 80 192.168.0.0/16
pinfo -n -iR 10000 -Pn -p 80
""")