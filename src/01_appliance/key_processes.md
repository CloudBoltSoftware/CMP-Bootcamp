# Key Processes

## `httpd`
* Apache httpd
* Managed via `apachectl` or `systemctl`
* `apachectl` can be used to get more information about apache
    * `apachectl -v`
* To restart httpd (and thus Django):
    * `systemctl restart httpd`

## `supervisord`
* Manages the execution of the Job Engine
* Controlled via `supervisorctl`
* To restart the job engine:
  * `supervisorctl restart jobengine:*`
  * Caution: This will kill running jobs

## `memcached`
* Key-value store
* Session cache
* Rarely needs attention

## `jobengine.pyc`
* Job engine worker
* Managed with supervisord (see above)

## `mysqld`
* MySQL Database worker process
* Can be restart with:
    * `systemctl restart mysql`

## `postgres`
* PostgreSQL database process