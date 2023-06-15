# CloudBolt Parameters
* Core to CloudBolt CMP is the concept of Custom Fields, or as they're presented in the UI: Parameters
* Used to attach data (Custom Fields) to CloudBolt Objects such as Servers, Resources, Environments, & Groups.
* Can be shown as part of a CloudBolt Object's parameters view by setting parameter's "Show on Objects" to: True
* Can be displayed as an Attribute on a CloudBolt Object's detail view by enabling "Show as Attribute"
* Can be applicable to any Server Object by enabling "Available to all Servers".
  * Server Lock
  * Use private key for SSH Sessions
  * Use tech-specific execution 
* Note: "Show as Attribute" must be disabled for "Available to all Servers" parameters.
* Are equivalent to CustomFields in Python, therefore programmatically accessible as previously demonstrated.
* Parameters set on Environments and Groups will be attached automatically to Servers provisioned

## Global Options
* Can be set at the Parameter level
* Will be overridden if any Group or Environment options are specified for the parameter

## Parameter Inheritance/Precedence
* When Parameter options are set for a Group and Environment, CloudBolt displays the union of Group and Environment options
* If a parameter is required, and conflicting values are set for the selected Environment and Group, the user must choose from the union of these options.

## Parameter Dependencies
* Parameters can be linked to be dependent on another parameter or OS Family
* Two types of dependencies: 
    * Show/Hide
    * Regenerate Options
* Show/Hide dependencies
    * Use one Parameter to determine when another Parameter should be displayed
    * Common use-case is to have a Boolean Parameter, that when checked displays an additional parameter
* Regenerate Options
    * Given a control value, force the regeneration of options for a dependent parameter

