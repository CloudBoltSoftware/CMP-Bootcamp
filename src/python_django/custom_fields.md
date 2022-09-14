# Custom Fields

Custom fields are used to add additional information to CloudBolt objects in a way that does not require changes to the underlying database (migrations). 

In a lot of ways, custom fields behave a lot like tags, but have the added benefit of being able to defined with a specific datatype. 

* String
* Integer
* IP Address
* Date & Time
* Multi-line Text
* Encrypted Text
* Code
* Boolean
* Decimal
* Network
* Password
* Tuple
* LDAPUtility
* URL
* NSX Scope
* NSX Edge
* DiskStorage
* File Upload

The datatype is a hint to CMP on how the data should be collected, displayed, and presented. 

Most model objects in CloudBolt CMP can have custom fields. 

![Relationship between Objects, Custom Fields, and Custom Field Values](../assets/Custom%20Fields.png)

Custom Fields are very closely related to parameters which will be discussed in the next Chapter.

Custom fields can also be programmatically attached to objects such as Resources, Servers, and more.

