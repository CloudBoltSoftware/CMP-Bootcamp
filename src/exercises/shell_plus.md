# EXERCISE: Starting and Using `shell_plus`

## Use-case
You saw Server method used in a CloudBolt plugin called `execute_script`, and you'd like to know more about what arguments this function accepts.

## Solution
Login to the CLI on your CloudBolt CMP appliance and start `shell_plus` to query the `run_script` function for more information.

1. Login to your CB CMP instance as root.
2. Start `shell_plus` with: `/opt/cloudbolt/manage.py shell_plus`
3. Find all object starting with "Se" by typing: `Se` then [TAB]
4. Select `Server` and type `.` (period) and press [TAB]
   * A list of methods for the Server object is listed
4. Continue typing `exe` and press [TAB]
   * Note the name `execute_script` function completes
5. Add a `?` to the end of Server.execute_script and press [ENTER]
   * Note the docstring and parameter details for the execute_script method is displayed.


This also works for Python functions, for instance the `run_command` function in the `utilities.run_command` module:

1. Import the utilities.run_command module by typing (hint: use autocomplete!): `from utiliites.run_command import run_command` 
   * Note: Only Django Models are loaded automatically at startup by `shell_plus`. Standard Python modules must still be explicitly imported.
2. Now that the `run_command` function from the `utilities.run_command` module, query its docstring with: `run_command?` [ENTER]
3. Now call `run_command` to run a local command on the CloudBolt CMP appliance by typing: `run_command('ls /')`.



