# My MAC address
# Displays the Media Access Code (MAC) of a Raspberry Pi

import sys

# ask user for the adapter for which the MAC is required.

adapter = input("\nEnter the adapter for which you require the MAC code: ")

dir_start = str("/sys/class/net/")

file_name = str("/address")

location = dir_start + adapter + file_name

# Read MAC from file
myMAC = open(location).read()

# Echo to screen
print("MAC:", myMAC)

