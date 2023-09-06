#!/bin/python
PACKAGES_TO_INSTALL = "{{ PACKAGES_TO_INSTALL }}"

import subprocess

# Convert multi-value field to space-separated list in cmd
packages = eval(PACKAGES_TO_INSTALL)
packages = " ".join(packages)
cmd = "yum install -y {}".format(packages)

# Print the command we're running to the log
print("RUNNING: {}".format(cmd))

# Run our command and capture output
cmd_output = subprocess.check_output(cmd, shell=True)
print(cmd_output)
