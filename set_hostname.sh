#!/bin/bash
# resets hostname to something different than AWS provided
# and required by jenkins swarm slaves to start

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/X11
HOSTNAME=jenkinsswarm

echo "original hostname is:" > /root/jenkinsswarm/sethostname.log
cat /etc/hostname >> /root/jenkinsswarm/sethostname.log
echo "" >> /root/jenkinsswarm/sethostname.log

echo $HOSTNAME > /etc/hostname
/etc/init.d/hostname start >> /root/jenkinsswarm/sethostname.log

echo "new hostname is:" >> /root/jenkinsswarm/sethostname.log
hostname >> /root/jenkinsswarm/sethostname.log
~                                               