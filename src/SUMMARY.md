# CloudBolt CMP Bootcamp
* [Introduction](introduction.md)
* [Prerequisites](prerequisites.md)
* [Getting Started](getting_started.md)

## 1. The CloudBolt Appliance
- [Application Architecture](appliance/architecture.md)
- [Deployment Scenarios](appliance/deployment-arch.md)
- [Deployment](appliance/deployment.md)
  - ***[EX: CMP on Public Cloud Marketplaces](exercises/marketplaces.md)***
- [Upgrades](appliance/upgrades.md)
  - ***[EX: Upgrade CMP*](exercises/upgrade.md)***
- [Getting to know the Appliance](appliance/gettingtoknow.md)
  - ***[EX: Explore the CMP Appliance](exercises/explore_appliance.md)***
  - ***[EX: Logging](exercises/logging.md)***
- [Useful CLI Commands](appliance/cli_commands.md)
- [Key Processes](appliance/key_processes.md)
- [Initial Setup](appliance/initial_setup.md)


## 2. Python and Django
- [Intro to Django](python_django/django_intro.md)
- [Django Management Commands](python_django/commands.md)
  - ***[EX: View Django Management Commands](exercises/commands.md)***
- [Shell Plus](python_django/shell_plus.md)
  - ***[EX: Start shell plus](exercises/shell_plus.md)***
- [Object Relational Model](python_django/orm.md)
  - ***[EX: Query and Update CMP Objects](exercises/models.md)*** (IN PROGRESS)
- [Database Migrations](python_django/migrations.md)
- [Custom Fields](python_django/custom_fields.md)
  - ***[EX: Working with Custom Fields](exercises/accessing_cfs.md)***
  - ***[Ex: Creating and Attaching CFs](exercises/creating_cfs.md)***


## 3. CloudBolt Object Model
- [Resource Handlers](cb_model/resourcehandlers.md)
  - ***EX: Connect to AWS***
  - ***EX: Connect to Azure***
- [Images & Templates](cb_model/images_templates.md)
    - [Common Azure Images](cb_model/azure_images.md)
    - ***EX: Import images***
- [OS Builds](cb_model/osbuilds.md)
  - ***EX: Manage OS Builds***
- [Networks](cb_model/networks.md)
    - ***EX: Import Networks***
- [Environments](cb_model/environments.md)
  - ***EX: Manage auto-created Environments***
- [Groups](cb_model/groups.md)
  - ***EX: Create Groups***
  - ***EX: Setup Group Approvals***
- [Parameters](cb_model/parameters.md)
  - ***EX: Parameter Behavior Review***
- [Pre-Configurations](cb_model/preconfigs.md)
  - ***EX: Create Server Size Pre-configuration***
- [Jobs & Orders](cb_model/jobs_orders.md)
  - ***EX: Explore Object Model for an Order***
- [Remote Script Execution](cb_model/remote_scripts.md)
  - ***EX: Configure Remote Scripting***

## 4. Orchestration
- Actions
    - CB Plugins
    - Remote Scripts
    - Webhooks
    - Email Actions
    - Other (Terraform, File Copy)
- Orchestration Actions
  - ***EX: User Data for Agent Install*** 
  - ***EX: Create a Monitoring Action***
  - ***EX: Handle Expired Servers***
- Parameter Orchestration
  - ***EX: Dependent Fields***
  - ***EX: Generated Options*** 
- Resource/Server Actions
  - ***[EX: Create a Server Action](exercises/server_action.md)***
- Multichannel Alerts
  - ***[EX: Setup an MCA target](exercises/mca.md)***
- Recurring Jobs
  - ***EX: Create a Recurring Job***
- Rules

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


