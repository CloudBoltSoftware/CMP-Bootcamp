# `shell_plus` Django Command

Running `/opt/cloudbolt/manage.py shell_plus` starts a Python shell inside the Django runtime. This means all Django apps are loaded and the database is available for ORM access. `shell_plus` is indispensable when developing scripts and extensions for CloudBolt CMP. Not only does it allow you to test Python code, but it's also a live reference that developers can use to query functions and objects for documentation on their use.

## Startup 
When starting `shell_plus`, the first thing it will do is load the Django project settings and then import all model objects defined in the current project. This is a `shell_plus` convenience and means there's no need to manually import these objects within `shell_plus`. Keep in mind, when running a Python script outside of shell_plus you will need to start the Django environment and explicitly import any models in your script.

If there are any issues with settings or problems loading any Django applications, `shell_plus` will not load. While this _can_ be frustrating since `shell_plus` is the first place one looks where startup issues, generally speaking `shell_plus` will yield a more useful error.

## Documentation
`shell_plus` has built-in functionality for the auto-completion of objects, methods, and functions. It also can be used to view function docstrings and parameter lists which can be very useful in cases where one may not necessarily know what parameters are expected. Customers often access where they can get documentation on objects -- `shell_plus` is a great place. Another place is directly from their CB CMP instance at https://HOSTNAME/alladmin/doc/models/.





