# Upgrading CloudBolt CMP

## Use Case
A customer has a CloudBolt CMP instance deployed in their AWS Public Cloud and would like to update via command line.

## Solution
Login to the CloudBolt CMP instance via SSH, download the latest upgrader, and run the upgrader.

1. Login to cbpl-controller, fetch your private key, and save to:
    * `~/.ssh/cbpl-123456.pem`
1. Set the appropriate file mode on your key
    * `chmod 600 ~/.ssh/cbpl-213456.pem`
1. Login to your CloudBolt instnace via SSH using you private key
    * `ssh -i ~/.ssh/cbpl-123456.pem centos@cbpl-123456.poc.cloudbolt.io`
2. Once on your instance, download the latest upgrader:
    * `wget https://downloads.cloudbolt.io/cloudbolt-upgrader-latest.tgz`
3. Expand the upgrader:
    * `tar xvf cloudbolt-upgrader-latest.tgz`
4. Start the upgrader:
    * `./upgrade-cloudbolt.sh`

