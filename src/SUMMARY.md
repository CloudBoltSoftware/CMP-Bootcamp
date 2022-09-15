# CloudBolt CMP Bootcamp

* [Introduction](introduction.md)
* [Prerequisites](prerequisites.md)
* [Getting Started](getting_started.md)

## The CloudBolt Appliance
- [Application Architecture](appliance/architecture.md)
- [Deployment Scenarios](appliance/deployment-arch.md)
- [Deployment](appliance/deployment.md)
  - ***[EX: CMP on Public Cloud Marketplaces](exercises/marketplaces.md)***
- [Upgrades](appliance/upgrades.md)
  - ***EX: Upgrade CMP*** (TODO)
- [Getting to know the Appliance](appliance/gettingtoknow.md)
  - ***[EX: Explore the CMP Appliance](exercises/explore_appliance.md)***
  - ***[EX: Logging](exercises/logging.md)***
- [Useful CLI Commands](appliance/cli_commands.md)
- Key Processes (TODO)
- [Initial Setup](appliance/initial_setup.md)


## Python and Django
- [Intro to Python](python_django/python_intro.md) (todo)
- [Intro to Django](python_django/django_intro.md)
- [Django Management Commands](python_django/commands.md)
  - ***[EX: View Django Management Commands](exercises/commands.md)***
- [Shell Plus](python_django/shell_plus.md)
  - ***[EX: Start shell plus](exercises/shell_plus.md)***
- [Object Relational Model](python_django/orm.md)
  - ***[EX: Query and Update CMP Objects](exercises/models.md)*** (IN PROGRESS)
- [Database Migrations](python_django/migrations.md) (IN PROGRESS)
- [Custom Fields](python_django/custom_fields.md)
  - ***[EX: Working with Custom Fields](exercises/accessing_cfs.md)***
  - ***[Ex: Creating and Attaching CFs](exercises/creating_cfs.md)***


## Cloudbolt Object Model

- [Resource Handlers](cb_model/resourcehandlers.md)
  - ***EX: Connect to AWS and Azure***
  - Images & Templates
    - ***EX: Import images***
  - Networks
    - ***EX: Import Networks***
- [OS Builds](cb_model/osbuilds.md)
  - ***EX: Manage OS Builds***
- Remote Script Execution
  - Credential Management
  - ***EX: Configure Remote Scripting***
- On-Prem Remote Scripting
  - Cloud-based Remote Scripting
- [Environments](cb_model/environments.md)
  - ***EX: Manage auto-created Environments***
  - Tech-Specific Parameters
  - Environment Parameters
    - Global vs. Local
    - Required Parameters
    - Input Validation
    - Parameter Dependencies
- Groups
  - Quotas
  - Group Parameters
- Resources
- Jobs & Orders

## AuthN, AuthZ, and SSO

- AuthN vs AuthZ
- LDAP/Active Directory Integration
  - Group/Role Mappings
    - ***EX: Setup AD Group Mappings***
- SSO/SAML2
  - IdPs vs SPs
  - ***EX: SSO Integration***

## Orchestration

- [Actions](orchestration/actions.md)
    - CB Plugins
    - Remote Scripts
    - Webhooks
    - Email Actions
- Resource/Server Actions
  - ***EX: Create a Server Action***
  - ***EX: Create a Resource Action***
- [Multichannel Alerts](orchestration/mca.md)
  - ***EX: Setup an MCA target***
- Orchestration Actions
- Recurring Jobs
- Rules
- Remote Script Execution

## XaaS (Anything-as-a-Service)
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
- Kubernetes

## Extending CloudBolt
- Content Library
- XUI Plugins
  - Custom Reports
  - Dashboard Widgets
  - Tab Extensions
  - Admin Extensions


