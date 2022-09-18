# Upgrading CloudBolt CMP

## Use Case
A customer has a CloudBolt CMP instance deployed in their AWS Public Cloud and would like to update via command line.

## Solution
Login to the CloudBolt CMP instance via SSH, download the latest upgrader, and run the upgrader.

1. Using your instance private key, SSH to your CloudBolt instance.
2. Once on your instance, download the latest upgrader:
    * `wget https://downloads.cloudbolt.io/cloudbolt-upgrader-latest.tgz`
3. Expand the upgrader:
    * `tar xvf cloudbolt-upgrader-latest.tgz`
4. Start the upgrader:
    * `./upgrade-cloudbolt.sh`

