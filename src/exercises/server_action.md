# Exercise: Create a Server Action

## Use-Case
We would like to provide owners of Linux servers an easy way to patch their servers.

## Solution
Provide a Server Action that when executed, will run a Remote Script on a target server to patch the target server(s)

## Implementation

1. Go to "Admin>Server Actions" and click "Add a Server Action/Create New".

2. Click "Remote Script", then click "Add a new remote Script".

3. In the "Add Remote Script Action" dialog, set the following values, then click "Create"
 * Name: Patch Server
 * Description: This server action will patch target Linux servers.
 * Shared: Check
 * OS Families: 
   * Linux -> Amazon Linux
   * Linux -> CentOS
   * Linux -> Red Hat
 * Run with sudo on *nix: Checked

5. Expand the new Remote Script titled "Patch Server", then enter the following script:
   ```
   #!/bin/bash
   yum update -y
   ```

6. Click the "Save code" button at the bottom of the code editor. 

7. Click the "Edit" button located on the top right of the server action panel,

8. Set "Extra classes" to: fas fa-bolt and then click "Save".

## Usage

Go to a CentOS Server and click the "Patch Server" item in the Server Action menu on the left of the Server Details page.

When a job is created, click the link the notification to track its progress.





