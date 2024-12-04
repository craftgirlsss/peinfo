#!/usr/bin/env python
from src.header import Header
from src.argument_handler import *
from src.helpers import *
from scapy.all import IP, TCP, send

if __name__ == "__main__":
    clear_terminal()
    header = Header()
    ArgumentHandler()