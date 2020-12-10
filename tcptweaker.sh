#!/bin/bash
tput setaf 7 ; tput setab 4 ; tput bold ; printf '%35s%s%-20s\n' "TCP Tweaker 1.0" ; tput sgr0
if [[ `grep -c "^#PH56" /etc/sysctl.conf` -eq 1 ]]
then
	echo ""
	echo "TCP Tweaker network settings have already been added to the system!"
	echo ""
	read -p "Do you want to remove the TCP Tweaker settings? [y/n]: " -e -i n answer0
	if [[ "$answer0" = 'y' ]]; then
		grep -v "^#PH56
net.ipv4.tcp_window_scaling = 1
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.ipv4.tcp_rmem = 4096 87380 16777216
net.ipv4.tcp_wmem = 4096 16384 16777216
net.ipv4.tcp_low_latency = 1
net.ipv4.tcp_slow_start_after_idle = 0" /etc/sysctl.conf > /tmp/syscl && mv /tmp/syscl /etc/sysctl.conf
sysctl -p /etc/sysctl.conf > /dev/null
		echo ""
		echo "TCP Tweaker network settings have been successfully removed."
		echo ""
	exit
	else 
		echo ""
		exit
	fi
else
	echo ""
	echo "This is an experimental script. Use at your own risk!"
	echo "This script will change some network settings"
	echo "of the system to reduce latency and improve speed."
	echo ""
	read -p "Continue with the installation? [y/n]: " -e -i n answer
	if [[ "$answer" = 's' ]]; then
	echo ""
	echo "Modifying the following settings:"
	echo " " >> /etc/sysctl.conf
	echo "#PH56" >> /etc/sysctl.conf
echo "net.ipv4.tcp_window_scaling = 1
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.ipv4.tcp_rmem = 4096 87380 16777216
net.ipv4.tcp_wmem = 4096 16384 16777216
net.ipv4.tcp_low_latency = 1
net.ipv4.tcp_slow_start_after_idle = 0" >> /etc/sysctl.conf
echo ""
sysctl -p /etc/sysctl.conf
		echo ""
		echo "TCP Tweaker network settings have been successfully added."
		echo ""
	else
		echo ""
		echo "The installation was canceled by the user!"
		echo ""
	fi
fi
exit
