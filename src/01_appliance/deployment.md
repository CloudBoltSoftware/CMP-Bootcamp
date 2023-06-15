# CMP Deployment

* The most common deployment scenarios for CMP include:
  * Deploying the virtual appliance on-prem in customer vCenter environment
  * Using a Public Cloud Marketplace image to deploy to AWS or Azure
  * Installing directly to a CentOS-7 OS from Installer


## On-Prem Virtual Appliance
### vCenter

* OVA deployment into vCenter
* Latest GA release is always available at:
  * https://downloads.cloudbolt.io/cloudbolt-latest.ova

### Other Hypervisor Environments
* In rare cases we may be asked to provide a QCOW image
* For deployment in OpenStack and Nutanix
* Can also convert to Hyper-V format
* Can be created from 

## Public Cloud Marketplace
### AWS

* Available in AWS Marketplace
  * https://aws.amazon.com/marketplace/pp/prodview-tuvzf2rewwcy4
* BYOL: Bring-your-own-license
* Private offers are available

### Azure
* Available in Azure Marketplace
  * https://azuremarketplace.microsoft.com/en-us/marketplace/apps/cloudboltsoftware1639523402532.cloudbolt-2022-2-3
* BYOL: Bring-your-own-license
* Private offers are available

# EXERCISE: CMP on Public Cloud Marketplaces


## Installing CMP from Installer
* Latest release always available from:
  * https://downloads.cloudbolt.io/cloudbolt-installer-latest.tgz
* Will install directly to a server running a RHEL7 compatible OS
  * CentOS-7, RHEL7, Oracle Enterprise Linux 7, and Amazon Linux 
* Assumes OS media is available and OS install is configured to use this media
  * Disk image
  * Satellite server

