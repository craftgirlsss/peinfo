import sys
from src.help import Help
from src.nmap_project import *
from src.ddos_project import *

class ArgumentHandler:
    def __init__(self):
        self.argumentHandler()

    def argumentHandler(self):
        if(len(sys.argv)-1 == 0):
            Help.exampleUsage()
        if(sys.argv[1] == "-n"):
            NmapProject(arguments=sys.argv, target=len(sys.argv))
        elif(sys.argv[1] == "-d"):
            DDoS(target="helow")
        elif(sys.argv[1] == "-h"):
            Help.exampleUsage()
        else:
            Help.exampleUsage()