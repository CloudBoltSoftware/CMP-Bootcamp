# Upgrading CloudBolt CMP

## Use Case
A customer has a CloudBolt CMP instance deployed in their AWS Public Cloud and would like to update via command line.

## Solution
Login to the CloudBolt CMP instance via SSH, download the latest upgrader, and run the upgrader.

1. Login to [cbpl-controller.poc.cloudbolt.io](https://cbpl-controller.poc.cloudbolt.io/) via Microsoft 365 account
2. From the top navigation bar, click on **Resources** > **CloudBolt Instances** and click on your CMP instance
3. Click on **Fetch Private Key** action
    * A Job will run.  Click on the Job to get your Private Key from the logs.
5. Save your private key to your local laptop:
    * `~/.ssh/cbpl-123456.pem` - replace *123456* with your instance ID
6. Set the appropriate file mode on your key:
    * `chmod 600 ~/.ssh/cbpl-123456.pem` - replace *123456* with your instance ID
7. Login to your CloudBolt instance via SSH using your private key
    * `ssh -i ~/.ssh/cbpl-123456.pem centos@cbpl-123456.poc.cloudbolt.io` - replace *123456* with your instance ID
    * `sudo su -`
    * `cd /var/tmp`
8. Download the latest upgrader:
    * `wget https://downloads.cloudbolt.io/cloudbolt-upgrader-latest.tgz`
9. Expand the upgrader:
    * `tar xvf cloudbolt-upgrader-latest.tgz`
10. Start the upgrader:
    * `cd cloudbolt_upgrader*`
    * `./upgrade_cloudbolt.sh`

CloudBolt will upgrade to the new version[^1].

[^1]: [Docs: Upgrading CloudBolt](https://docs.cloudbolt.io/articles/#!cloudbolt-latest-docs/upgrading-cloudbolt)
