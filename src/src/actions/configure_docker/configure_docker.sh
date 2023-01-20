#!/bin/bash
export PATH=/usr/bin:/sbin

# Disable SELinux support in docker daemon
sed -i 's/\(--selinux-enabled\) /\1=false /g' /etc/sysconfig/docker /etc/sysconfig/docker

# Start and enable docker daemon
systemctl enable docker
systemctl start docker

