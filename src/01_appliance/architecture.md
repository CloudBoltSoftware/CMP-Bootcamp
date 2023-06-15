# CMP Application Architecture

## Major Application Components

* Apache httpd
  * Handles inbound web requests
* Python 3.9 runtime
  * Runs Django environment and WSGI
* Django Application
  * Hosts all Django applications
* Memcache
  * User session and key/value storage
* Supervisord
  * Manages execution of Job Engine
* Database Server
  * PostgreSQL (Default for new installs)
  * MySQL 5.7
* Guacd
  * Manages remote terminal/desktop sessions


## Appliance Architecture

![CloudBolt CMP Appliance Architecture](../assets/Appliance%20Architecture.png)