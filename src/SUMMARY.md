# CloudBolt CMP Bootcamp
* [Introduction](00_introduction/introduction.md)
* [Prerequisites](00_introduction/prerequisites.md)
* [Getting Started](00_introduction/getting_started.md)

## 1. The CloudBolt Appliance
- [Application Architecture](01_appliance/architecture.md)
- [Deployment Scenarios](01_appliance/deployment-arch.md)
- [Deployment](01_appliance/deployment.md)
  - ***[EX: CMP on Public Cloud Marketplaces](exercises/marketplaces.md)***
- [Upgrades](01_appliance/upgrades.md)
  - ***[EX: Upgrade CMP*](exercises/upgrade.md)***
- Connecting to the Appliance
- [Getting to know the Appliance](01_appliance/gettingtoknow.md)
  - ***[EX: Explore the CMP Appliance](exercises/explore_appliance.md)***
  - ***[EX: Logging](exercises/logging.md)***
- [Useful CLI Commands](01_appliance/cli_commands.md)
- [Key Processes](01_appliance/key_processes.md)
- [Initial Setup](01_appliance/initial_setup.md)


## 2. Python and Django
- [Intro to Django](02_python_django/django_intro.md)
- [Django Management Commands](02_python_django/commands.md)
  - ***[EX: View Django Management Commands](exercises/commands.md)***
- [Shell Plus](02_python_django/shell_plus.md)
  - ***[EX: Start shell plus](exercises/shell_plus.md)***
- [Object Relational Model](02_python_django/orm.md)
  - ***[EX: Query and Update CMP Objects](exercises/models.md)***
  - ***EX: Generate ERDs***
- [Database Migrations](02_python_django/migrations.md) (internal)
- [Custom Fields](02_python_django/custom_fields.md)
  - ***[EX: Accessing Custom Fields](exercises/accessing_cfs.md)***
  - ***[Ex: Creating and Attaching CFs](exercises/creating_cfs.md)***


## 3. CloudBolt Object Model
- [Resource Handlers](03_cb_model/resourcehandlers.md)
  - ***EX: Connect to vCenter***
  - ***EX: Connect to AWS***
  - ***EX: Connect to Azure***
- [Images & Templates](03_cb_model/images_templates.md)
    - [Common Azure Images](03_cb_model/azure_images.md)
    - ***EX: Import images***
- [OS Builds](03_cb_model/osbuilds.md)
  - ***EX: Manage OS Builds***
- [Networks](03_cb_model/networks.md)
- [Environments](03_cb_model/environments.md)
- [Groups](03_cb_model/groups.md)
  - ***EX: Create Groups***
  - ***EX: Setup Group Approvals***
- [Parameters](03_cb_model/parameters.md)
  - ***EX: Tech-specific Parameters***
  - ***EX: CloudBolt Parameters***
  - ***EX: Parameter Behavior Review***
- [Pre-Configurations](03_cb_model/preconfigs.md)
  - ***EX: Create Server Size Pre-configuration***
- [Jobs & Orders](03_cb_model/jobs_orders.md)

## 4. Orchestration
- Actions
- Actions: CloudBolt Plugins
- [Remote Script Execution](03_cb_model/remote_scripts.md)
  - ***EX: vCenter Remote Scripting***
  - ***EX: AWS Remote Scripting***
  - ***EX: Azure Remote Scripting***
- Actions: Remote Scripts      
- Orchestration Actions
  - ***EX: User Data for Agent Install*** 
  - ***EX: Create a Monitoring Action***
  - ***EX: ConnectionInfo Objects***
  - ***EX: Handle Expired Servers***
- Parameter Orchestration
  - ***EX: Parameter Change***
  - ***EX: Dependent Fields***
  - ***EX: Generated Options***
  - ***EX: Tagging***
- Resource/Server Actions
  - ***[EX: Create a Server Action](exercises/server_action.md)***
- Multichannel Alerts
  - ***[EX: Setup an MCA target](exercises/mca.md)***
- Recurring Jobs
  - ***EX: Create a Recurring Job***

## 5. XaaS (Anything-as-a-Service)
- Catalog
- XaaS Resource Types
  - Services
  - Servers
  - User-Defined
- Blueprints
  - Object model
- Parameters Revisitied
  - Generated Parameters
- Teardown & Discovery
- Action Blueprint Items
  - Action Inputs
- Terraform Blueprint Items

## 6. Extending CloudBolt
- Content Library
- XUI Plugins
  - Custom Reports
  - Dashboard Widgets
  - Tab Extensions
  - Admin Extensions


