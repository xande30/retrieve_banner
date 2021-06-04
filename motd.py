#!/usr/bin/env python
import socket
from termcolor import colored


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(3)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner

    except:
        return


def main():
    port = 22
    ip = input("Please input your IP ADDRESS: ")
    banner = str(retBanner(ip, port))
    if banner:
        print(colored("[+]" + ip + ": " + banner, 'magenta'))


main()
