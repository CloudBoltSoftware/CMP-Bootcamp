# Groups
* Used to organize resources and users in CloudBolt CMP
* Users are associated with Groups via Roles
  * Each Role has its own set of system-defined permissions
  * Roles can be defined and managed by CB Admin
* Groups determine what Environments a User can access
* Permissions are not inherited unless this feature is enabled

## Default Roles

* Requestor
  * Can order new Resources
* Viewer
  * Can only view Resources
  * Good for managers, oversight teams
* Group Admin
  * Can manage Group users
  * Add/Remove users and set roles
* Resource Admin
  * Can access any Resource in the Group
* Approver
  * Can approve order requests
* Delegate Server Owner
  * Allows more than one user to act as owner of a Resource

## Parameters
* Like Environments, Parameters can be assigned to Groups
* Group parameters are good for enforcing behavior
  * Expiration Date

## Quotas
* Quotas can be set at any group level
* A quota for a given group can only be set if quota is available in the parent group
* Can be set to Mem, Disk, CPUs, # Servers, and Cost
  * Cost is based upon estimated cost

