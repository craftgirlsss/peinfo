from colorama import Fore, Back, Style

class Header:
    def __init__(self):
        self.display()

    def display(self):
        print(Fore.GREEN, """
                 _____     _____        __      
                |  __ \   |_   _|      / _|     
                | |__) |__  | |  _ __ | |_ ___  
                |  ___/ _ \ | | | '_ \|  _/ _ \ 
                | |  |  __/_| |_| | | | || (_) |
                |_|   \___|_____|_| |_|_| \___/                                  
""")
        print(Fore.WHITE, """
PeInfo v1.0 ( https://nextjiesdev.site )
              
PeInfo simple tool information gathering network port and DDoS Attack.
Usage: pinfo [Type Attack] [Options] [target specification]
        """)

