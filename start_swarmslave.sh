#!/bin/bash
#
# Jenkins-swarm Startup script for the Jenkins Swarm Slave
#

# URL path to your Jenkins Server
SWARMMASTER=http://10.0.0.4:8080

# Path to Java, and the java-swarm jar file
JAVA=/usr/bin/java
SWARMJAR=/root/jenkinsswarm/swarm-client-1.9-jar-with-dependencies.jar

# Swarm log file
SWARMLOG=/root/jenkinsswarm/swarm.log

# Name for this Jenkins Slave
SWARMUUID="Linux-`/usr/bin/uuidgen -r`"

# Description of this Slave
SWARMDESC="Jenkins Swarm Slave in Skytap on AWS"

# Labels to use when building
SWARMLABELS="LinuxSwarmSlave"

#Jenkins authentication
SWARMUSER=swarm
#SWARMPW=MmdbFCTb
SWARMPW=dasboot4

sleep 10 #added to ensure previous scripts have completed

# Start the Swarm Slave
$JAVA -jar $SWARMJAR -master $SWARMMASTER -name $SWARMUUID -description "$SWARMDESC" -labels "$SWARMLABELS" -username $SWARMUSER -password $SWARMPW >> $SWARMLOG 2>&1
