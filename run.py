#!/bin/bash while:do if ping -c 1 192.168.10.144 &> /dev/null then echo "Host is online" break fi sleep 5 done
