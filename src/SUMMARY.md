# CloudBolt CMP Bootcamp

* [Introduction](introduction.md)
* [Prerequisites](prerequisites.md)
* [Getting Started](getting_started.md)

## The CloudBolt Appliance
- [Application Architecture](appliance/architecture.md)
- [Deployment Scenarios](appliance/deployment-arch.md)
- [Deployment](appliance/deployment.md)
  - [On-Prem Virtual Appliance](appliance/deployment.md#onprem)
  - [Public Cloud Marketplace](appliance/deployment.md#marketplace)
  - ***[EX: CMP on Public Cloud Marketplaces](exercises/marketplaces.md)***
- [Upgrades](appliance/upgrades.md)
  - ***EX: Upgrade CMP***
- [Getting to know the Appliance](appliance/gettingtoknow.md)
  - ***[EX: Explore the CMP Appliance](exercises/explore_appliance.md)***
  - ***[EX: Logging](exercises/logging.md)***
- Key Processes
- [Initial Setup](appliance/initial_setup.md)


## Python and Django
- [Intro to Django](python_django/django_intro.md)
- [Django Management Commands](python_django/commands.md)
  - ***[EX: View Django Management Commands](exercises/commands.md)***
- [Shell Plus](python_django/shell_plus.md)
  - ***[EX: Start shell plus](exercises/shell_plus.md)***
- [Object Relational Model](python_django/orm.md)
  - ***[EX: Query and Update CMP Objects](exercises/models.md)***
- [Database Migrations](python_django/migrations.md)
- [Custom Fields](python_django/custom_fields.md)

## Cloudbolt Object Model

- Resource Handlers
  - ***EX: Connect to AWS and Azure***
  - Images & Templates
    - ***EX: Import images***
  - Networks
    - ***EX: Import Networks***
- OS Builds
  - ***EX: Manage OS Builds***
- Remote Script Execution
  - Credential Management
  - ***EX: Configure Remote Scripting***
- On-Prem Remote Scripting
  - Cloud-based Remote Scripting
- [Environments](cloudbolt_object_model/environments.md)
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

- Actions
    - CB Plugins
    - Remote Scripts
    - Webhooks
    - Email Actions
- Resource/Server Actions
  - ***EX: Create a Server Action***
  - ***EX: Create a Resource Action***
- Multichannel Alerts
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


