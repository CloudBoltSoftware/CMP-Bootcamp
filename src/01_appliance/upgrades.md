# Upgrading CMP

## Current GA Upgrader
* The most current GA upgrader is always available from:
  * https://downloads.cloudbolt.io/cloudbolt-upgrader-latest.tgz
* Updated when a release becomes GA (Generally Available)

## Nightly Upgrader Builds
* Available at:
  * https://downloads.cloudbolt.io/cloudbolt-upgrader-nightly.tgz
* Updated from the `develop` branch on a nightly basis
* This is the latest code from engineering
* Not fully QA'ed and may contain features not slated for next release

## Latest Release Candidate Upgraders
* Available at:
  * https://downloads.cloudbolt.io/cloudbolt-rc-latest.tgz
* Released nightly leading up to the next GA release


## Upgrading via the UI
* UI-based upgrade available in product at: `Admin` > `Version & Upgrade Info`
* Only to be used in a virtual appliance (everything on one server) deployment scenario
  * Do not use this method if CMP is running with separate DB server and/or components 

## Configuring the Upgrader
* The configuration for the CloudBolt CMP instance is in the upgraders archive and named `install_config`
* Essential for upgrading CMP in any scenario beyond a single appliance
* Most common settings edited are database connection details for PostgreSQL or MySQL
* It's ok to run the upgrader on multiple CB component servers.
  * Database migrations are only run ONCE per database configured in `install_config`
* By default, install_config will update the LOCAL database instance
  * Common error is to run the upgrader in a multi-server scenario without modifying this file
  * Upgrader runs without issue, but configures upgraded instance to use the local database
 
