# ARP_spoofer
- Sends ARP packets to manipulate the target computer's ARP cache in order to perform a man-in-the-middle attack

- Uses the scapy/scapy.all, time, and sys modules in python to manipulate the target's ARP table; thus, putting yourself in the middle of the packet transmission 

- Full credit to StationX for the [tutorial](https://courses.stationx.net/p/the-complete-python-for-hacking-and-cyber-security-bundle) that taught me this code 

## scapy/scapy.all
- Use this module to create an ARP request and set the destination to the broadcast MAC address (network scanner) 
- Send an ARP response to the target machine (every 2 seconds) claiming to be the router 
- Reset the target machine to the original ARP table once the attack is complete 

## time
- Use this module to send an ARP request every 2 seconds to reestablish the ARP poising 

## sys
- Use this module to stop the program by entering "control c" and display a message to the user

