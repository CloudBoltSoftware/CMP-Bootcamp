# OS Builds

* OS Builds (`externalcontent.models.OSBuild`) provide a level of indirection between an Operating System and the underlying provider template or image.
* This indirection is an important component of CloudBolt CMP support for multi-cloud blueprints. 
* By default, when an image is imported for a resource handler, a new OS Build is created that corresponds to the image.
* OS Builds provide a user-friendly name to users when building Blueprints or choosing an Operating System
  * Rather than seeing an AMI ID, which means little to end-users, they can be presented with an OS name such as CentOS-7.
* One limitation at this time is that no more than one image per resource handler can be associated with an OS build.
  * This means if you have 2 regions imported into AWS, each providing a CentOS-7 image, both images cannot be associated with the same OS Build.
  * Being addressed in Buttercup (2022.4.1)

 

