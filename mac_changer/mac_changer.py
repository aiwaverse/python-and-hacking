#!/usr/bin/env python

import subprocess
import optparse

def change_the_mac_address (interface, mac_address):
    print("[+] Changing MAC address for " + interface + " to " + mac_address)
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC Address")
parser.add_option("-m", "--mac", dest="new_address", help="New MAC Address for the interface")
(options, arguments) = parser.parse_args()
change_the_mac_address(options.interface, options.new_address)
