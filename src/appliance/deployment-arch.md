# Common Deployment Architectures 

## Single appliance
* Default deployment mode
* Great for POCs and Development environments
* Not ideal for production environments, but could work with ample compute and DR strategy

![Single appliance diagram](../assets/Scenario%201.png)

## Front-end with dedicated DB tier
* Ideal for small/medium Production (<5000 VMs; <100 DAUs) environments
* Database instance on CloudBolt appliance is not used
* Good connectivity between front-end server and database tier required
* No shared file systems required

![Front-end with DB diagram](../assets/Scenario%202.png)

## Multiple front-ends with dedicated DB tier
* Ideal for large (>5000 VMs; >100 DAUs) Production environments
* Requires a shared NFS filesystem between front-end servers
* Good connectivity between all servers and storage is required

![Multiple frontends diagram](../assets/Scenario%203.png)

## Cloud Native Deployment
* Ideal for large production environments
* Can leverage server-based or serverless PostgreSQL cloud services
  * AWS RDS PostgreSQL
  * Azure Database for PostgreSQL
* Frontend servers run on virtual machines
* Shared storage amongst VMs is still required
  * AWS EFS
  * Azure Files
* Good option for multi-availability zones, scaling, and HA

![Multiple frontends diagram](../assets/Scenario%204.png)
