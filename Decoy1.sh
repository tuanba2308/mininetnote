#!/bin/sh
ip="10.0.0.6"
hping3 -c 100000 -d 10 -w 64 -p 4444 -i u10000 $ip
