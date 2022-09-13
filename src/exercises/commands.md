# EXERCISE: Django Commands

Use-Case: A customer would to export their entire CloudBolt environment including static files, database, and configuration.

Solution: Access the CLI on the CloudBolt server and run then cb_export management command. The resulting file can then be imported using the cb_import command into another CloudBolt instance.

1. Login to your CloudBolt instance.
2. Ensure you're running as root: `sudo su -`
3. Run the cb_export command: `/opt/cloudbolt/manage.py cb_export`
4. (theoretical) Import to another CloudBolt instance using the cb_import command.

