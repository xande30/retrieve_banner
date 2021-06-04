#!/usr/bin/env python

import socket
from termcolor import colored


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return


def main():
    ip = input(colored("Please input your ip address: \n", 'blue'))
    for port in range(1, 100):
            banner = str(retBanner(ip, port))
            if banner:
                print(colored("[+]" + ip + "/" + str(port) + ": " + banner.strip('\n'), 'green'))


main()
