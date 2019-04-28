#!/usr/bin/env python

import subprocess

interface = input("New interface > ")
new_address = input("New MAC address > ")
print("[+] Changing MAC address for " + interface + " to " + new_address)
subprocess.call("sudo ifconfig " + interface + " down", shell=True)
subprocess.call("sudo ifconfig " + interface + " hw ether " + new_address, shell=True)
subprocess.call("sudo ifconfig " + interface + " up", shell=True)
