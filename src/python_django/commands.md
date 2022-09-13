# Django Commands

Much of the functionality provided by the Django framework is exposed via Django Commands that are executed against a current Django project from the CLI. In a fresh Django install, this includes creating new projects/applications, managing the project database, and managing users. Additional commands can be added in the form of new commands from third-party libraries and the current application.

## `/opt/cloudbolt/manage.py` 

`manage.py` is the main entry point and Python script for executing any Django command. When executed, its first order of business is to bootstrap the Django runtime environment for the current project. Each Django project has its own `manage.py` script, but this script is rarely modified directly.

On systems where multiple Python runtimes are installed, it's important that `manage.py` is executed with the right Python command. The CB appliance ships with 2 python environments: One (`/usr/bin/python`) provided by the OS and used to support OS processes and functionality, and a second (`/usr/local/bin/python`) provided by CloudBolt to run CMP.

The OS-provided Python doesn't contain all the libraries and dependencies (including Django) to run CMP. It is essential that you always check that you're running the CloudBolt-provided Python interpreter. You will run into instances where customers are seeing errors when running the upgrader, or management commands because they're not running the correct Python interpreter.

To verify that you're running the right Python interpreter:

1. If you're not already running as root, login as root with: `sudo su -`
2. Run the command: `which python`
3. Verify that the response is: `/usr/local/bin/python`

If it is not, verify your PATH environment variable is correct and contains `/usr/local/bin` before `/usr/bin` by running `echo $PATH`.

## Running Commands

Django commands are passed as first arguments to `manage.py`. Running `manage.py` without arguments will print a list of available commands. Note this list is organized by Django Application as loaded from `settings.py`. By convention, management commands are located in `/management/commands` for a given application. Most CloudBolt-provided Django commands are provided by the `utilities` application, therefore the code for these commands is located in the: `utilities.management.commands` Python module located at `/opt/cloudbolt/utilities/management/commands/`.








