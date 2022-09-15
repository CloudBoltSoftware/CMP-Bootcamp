# Custom Fields

Custom fields are used to add additional information to CloudBolt objects in a way that does not require changes to the underlying database (migrations). 

In a lot of ways, custom fields behave a lot like tags, but have the added benefit of being able to defined with a specific datatype. A Custom Field's datatype is a hint to CMP on how the data should be collected, stored, and presented. 


| Datatype          | Type  | Notes
|-------------------|-------|----------------------------------|
| String            | STR   | Max length 975 characters        |
| Integer           | INT   || 
| IP Address        | IP    | String field with 256 max length |
| Date & Time       | DT    ||
| Multi-line Text   | TXT   ||
| Encrypted Text    | ETXT  | Stripped from logs and masked    |
| Code              | CODE  | Good for storing JSON            |
| Boolean           | BOOL  | True/False                       |
| Decimal           | DEC   ||
| Network           | NET   ||
| Password          | PWD   | Stripped from logs and masked    |
| Tuple             | TUP   |
| LDAPUtility       | LDAP  |
| URL               | URL   |
| NSX Scope         | NSXS  |
| NSX Edge          | NSXE  |
| DiskStorage       | STOR  |
| File Upload       | FILE  |


Most model objects in CloudBolt CMP are linked to CustomField objects via CustomFieldValue objects. CloudBolt objects that are most often associated with Custom Fields include:

* UserProfile
* Group
* Environment
* Server
* ResourceNetwork
* Resource
* ServiceBlueprint

![Relationship between Objects, Custom Fields, and Custom Field Values](../assets/Custom%20Fields.png)

Custom fields can be programmatically attached to these CloudBolt objects. Attaching CustomFields to Resources is an essential technique for tracking connections between multiple systems.

Custom Fields are very closely related to CloudBolt Parameters which will be discussed in the next Chapter.



