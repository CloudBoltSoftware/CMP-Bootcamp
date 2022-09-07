# CloudBolt CMP Bootcamp

* [Introduction](introduction.md)
* [Prerequisites](prerequisites.md)
* [Getting Started](getting_started.md)

## The CloudBolt Appliance

- [Architecture](appliance/architecture.md)
  - Diagram Review
- [Deployment](appliance/deployment.md)
  - On-Premises
    - vCenter
  - Cloud
    - AWS Marketplace
      - ***EX: Find CMP AWS Marketplace Image***
    - Azure Marketplace
      - ***EX: Find CMP Azure Marketplace Image***
  - Upgrades
    - ***EX: Upgrade CMP***
- Appliance Tour
  - ***EX: Explore CMP Appliance***
- [Initial Setup](appliance/initial_setup.md)

## Python and Django

- Django Management Commands
  - ***EX: View Django Management Commands***
- Shell Plus
  - ***EX: Start shell plus***
- Object Relational Model
  - ***EX: Query and Update CMP Objects***
- Logger Configuration

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

## Security

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


