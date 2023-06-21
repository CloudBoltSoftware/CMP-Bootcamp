#!/bin/bash
export PATH=/usr/bin:/sbin

# Add the docker-ce centos yum repo and install
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
