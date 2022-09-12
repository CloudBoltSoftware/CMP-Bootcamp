# EXERCISE: Managing Logger Levels

## Use-Case
The AWS boto3 SDK and urllib moduels are generating a lot of noise in a customer's application.log. They'd like to tune down logging for these module so that only errors are displayed. 

## Solution
Edit `/var/opt/cloudbolt/proserv/customer_settings.py` to override logging for the boto3 module so that instead of INFO or DEBUG logging, it will only log ERROR-level messages.
```
from settings import LOGGING, default_handlers

LOGGING["loggers"].update({
    "boto3": {
      "handlers": default_handlers,
      "level": "ERROR",
      "propagate": False
    },
    "urllib": {
      "handlers": default_handlers,
      "level": "ERROR",
      "propagate": False
    },
})
```
