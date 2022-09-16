# Resource Handlers

Resource Handlers model the connection between CloudBolt CMP and backend clouds and hypervisor management systems. CloudBolt supports over twenty different Resource Handlers including the most popular AMIGO (AWS, MS Azure, IBM, GCP, & Oracle) clouds and data center hypervisor management systems like vCenter, OpenStack, and Nutanix Acropolis.

As the mediator between backend providers, CloudBolt Resource Handlers serve as an adapter between the CloudBolt object model and the differences between these various providers. These differences most often start with authentication and expand to their APIs which, more often than not, are completely different. There's certainly an analogy here between printer drivers and these resource handlers.

Access to Resource Handler management is limited to CloudBolt Admins and Tenant Admins. These teams are tasked with providing access to these clouds and resources, therefore end-users rarely interact directly with resource handlers.


## Resource Handler Object Model

* Resource Handler models all inherit from the generic Resource Handler model. 
* Each concrete Resource Handler uses a wrapper object that encapsulates low-level API calls to the underlying provider.

![ResourceHandler object model](../assets/ResourceHandlers%20Object%20Model.png)

