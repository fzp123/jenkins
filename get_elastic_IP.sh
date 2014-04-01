#!/bin/sh
# get elastic IP address of self from AWS and print it
echo
echo "My Elastic IP is:"
/usr/bin/curl -s  http://169.254.169.254/latest/meta-data/public-ipv4 2>&1
echo 
echo
~       