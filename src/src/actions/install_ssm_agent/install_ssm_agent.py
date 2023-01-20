from common.methods import set_progress

SCRIPT = """#!/usr/bin/bash
yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm
systemctl enable amazon-ssm-agent
systemctl start amazon-ssm-agent
"""

def run(job, server, **kwargs):
    server.aws_user_data = SCRIPT
    server.save()
    return "SUCCESS", "", ""
