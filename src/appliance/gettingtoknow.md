# Getting to Know the CMP Appliance


## Key Directories

### `/opt/cloudbolt`
* Core product code that comprises a release is located here
* Completely replaced as part of the upgrade process
* No modifications should be made to code or settings here
* Part of the Python runtime path (PYTHONPATH)

### `/var/opt/cloudbolt`
* Instance specific data is stored here
* Not replaced by upgraders, but may be modified
* Shared amongst all servers via shared file system HA scenarios

### `/var/opt/cloudbolt/proserv`
* Customer-specific code goes here
* Not affected by upgraders
* Contains customer-specific settings (`customer_settings.py`)
* Part of the Python runtime path (PYTHONPATH)

### `/var/log/cloudbolt`
* All application and job logs are stored here
* NOT shared between instances in HA scenario
* Primary root application log located here for instance (`application.log`)

### `/var/log/cloudbolt/jobs`
* Shared via shared filesystem in HA deployment scenarios

### `/etc/httpd`
* Apache configuration files -- might be modified in the rarest of cases
* One case for modification is to install SSL certs by modifying `/etc/httpd/conf.d/


## Other CMP-Related Directories

### `/var/www/html/cloudbolt`
* Used to serve static files (images, js, css) via Apache
* Also used to receive uploaded files
* Shared across instances via shared filesystem in HA scenarios

### `/var/run/cloudbolt`
* Instance specific
* Contained PID files for processes
* Not too interesting

## Logging
* Logging in CMP is based upon the Python logging facility
* PLF is a extensible hierarchical logging system that connects "loggers" to "handlers"

### `/var/log/cloudbolt`
* The main CloudBolt Application log.

### `/var/log/cloudbolt/jobs`
* Subdirectory is shared to all instances in an HA deployment scenario
* This is so every instance, whether a job engine instance or front-end server, has access to job logs.
* Contains all job logs run by CloudBolt


### Logging Configuration
* Default logging configuration is stored in `/opt/cloudbolt/settings.py`
* Do not modify this file directly
* Override loggers in `/var/opt/cloudbolt/proserv/customer_settings.py`
* Loggers are identified by their corresponding python module names
  * django.util
  * saml2
  * resourcehandlers.aws.models
* A logger named `my_module` covers `my_module` and all submodules
  * `my_module`
  * `my_module.sub_module_a`
  * `my_module.sub_module_b`
  * `my_module.sub_module_b.sub_sub_module`
* Log Levels
  | Level  | Description                        |
  |------- |---------------                     |
  |DEBUG   |Most verbose. CMP in debug mode.    |
  |INFO    | CMP in non-debug (production) mode |
  |WARNING |                                    |
  |ERROR   |                                    |
  |CRITICAL|Least Verbose                       |
  |        |                                    |

 
### `/var/http/ssl_error_log`
* Apache httpd log
* Should be the first place you check if you see a generic "Server Error"
* Any Django startup errors/messages will appear here


> [EXERCISE: Logging Configuration](../exercises/logging.md)


## Crontab

## Supervisor

## Apache HTTPd


