#!/bin/bash
# Use: sudo iptables.sh <iface>

VBoxManage hostonlyif ipconfig vboxnet0 --ip 192.168.56.1
iptables -A FORWARD -o $1 -i vboxnet0 -s 192.168.56.0/24 -m conntrack --ctstate NEW -j ACCEPT;
iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT;
iptables -A POSTROUTING -t nat -j MASQUERADE;
# Drop spam attempts
iptables -A FORWARD -p tcp -m tcp --dport 25 -j DROP;
iptables -A FORWARD -p tcp -m tcp --dport 587 -j DROP;
iptables -A OUTPUT -p tcp --dport 587 -j DROP;
iptables -A OUTPUT -p tcp --dport 25 -j DROP;
sysctl -w net.ipv4.ip_forward=1
