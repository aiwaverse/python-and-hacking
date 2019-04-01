#!/usr/bin/env python3
import subprocess
interface = "enp3s0"
new_mac = "00:11:22:33:44:56"
print("Changing MAC adress for " + interface + " to: " + new_mac)
subprocess.call("sudo ifconfig " + interface + " down", shell=True)
subprocess.call("sudo ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("sudo ifconfig " + interface + " up", shell=True)

