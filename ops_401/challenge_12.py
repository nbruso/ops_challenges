# OPS401D10  Ops Challenge 11
# 01/23/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source: https://web.archive.org/web/20180826164313/https://infinityquest.com/python-tutorials/generating-a-range-of-ip-addresses-from-a-cidr-address-in-python/; https://chat.openai.com/share/48471212-55c9-46af-a98c-26d5cd1f7239; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-12/challenges/DEMO.md

#!/usr/bin/env python3

# Importing required libraries
from scapy.all import *  # Scapy for network operations
import ipaddress  # Used for handling IP addresses

# Function to get a list of IP addresses in a network
def list_all_addresses(network):
    try:
        # Create a network object from the given network string
        net = ipaddress.ip_network(network)
        # Return a list of all IP addresses in this network
        return list(net.hosts())
    except ValueError as e:
        # If there is an error (like a wrong network format), print the error
        print(f"Error: {e}")
        return []

# Main function of the script
def main():
    # Ask the user to choose between two modes
    choice = input("Choose mode:\n1. TCP Port Range Scanner\n2. ICMP Ping Sweep\n3. Exit\nEnter choice (1, 2, or 3): ")
    
    if choice == '1':
        # Placeholder for TCP Port Range Scanner functionality
        # Add the specific TCP Port Range Scanner code here
        print("TCP Port Range Scanner mode selected. Functionality to be implemented.")
    
    elif choice == '2':
        # If user chooses ICMP Ping Sweep
        network = input("Enter the network in CIDR format (e.g., 192.168.1.0/24): ")
        addresses = list_all_addresses(network)
        if addresses:
            print("IP addresses in the network:")
            for address in addresses:
                print(address)
        else:
            print("No addresses found or invalid network.")
    
    elif choice == '3':
        # If user chooses to exit
        print("Exiting the program.")
    
    else:
        # If user enters something other than 1, 2, or 3
        print("Invalid choice.")

# This makes sure the script runs the main function when you run the script
if __name__ == "__main__":
    main()
