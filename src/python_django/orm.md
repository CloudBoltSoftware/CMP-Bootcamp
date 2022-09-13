# Django ORM

The Django Object Relational Mapper (ORM) is one of the most powerful features of the Django framework as it provides an abstraction and management layer between the Python runtime and the underlying relational database. Django ORM supports many databases including the two primarily used with CloudBolt CMP: MySQL and PostgreSQL. 

For years, CloudBolt CMP shipped with and used MySQL 5.7, but recent licensing changes by Oracle compelled us to change the preferred database to PostgreSQL by default. For the time being, both databases are supports, but as time goes on and more customers move to PostgreSQL, MySQL support will be deprecated. All new CMP virtual appliances and installers will install PostgreSQL by default going forward. The fact we use Django ORM to provide a layer of isolation between our application code and the database is what allowed us to make this transition and continue to support both databases going forward.

In addition to insulating users from the underlying database -- each with its own interpretation of SQL -- Django ORM allows developers to work with Model objects using the same Python syntax and semantics as the rest of their code. The end-result being more developer productivity, more legible code, and increasingly more useful type-hinting.

## Model Documentation
The CloudBolt CMP data model is modeled using Django ORM. This means documentation for all of these models is generated automatically and is available from https://HOSTNAME/alladmin/doc/models/. This includes all attributes relationships between these model objects.

## Querying Model Objects
A common query is to return all rows from a table representing a specific business object. In terms of CloudBolt CMP, this might include Servers. Rather than writing SQL code and then translating tabular data to Python data types, we can do all this at once with a simple line of Python code: `servers = Server.objects.all()`. This queries the underlying database for all Server objects and returns them as an iterable Python type.

## Traversing Relationships
Working with related objects in Django ORM is also much simpler than with direct database/SQL access to the data. For the case where I have a many-to-one relationship, say between a Server (many) and Environment (one), I can simply reference the related reference using it's property. In this case… `environment`. So given a Server object s, to get the name of the Environment to which it's assigned I can write: `print(s.environment)`. This is much easier than dealing with SQL joins!

## Filtering Objects/Querysets
There are a couple of interesting ways to filter objects in Django ORM. Neither involves getting all objects from the database and iterating over every item checking a property for some condition.

### Filter
Django ORM Queryset objects include a method called filter that can be used to filter query results by field value in the Model and related Models.

For instance, building on the Server example above, I can return all active servers with: `Server.objects.filter(status='ACTIVE')`. The field I'm filtering on corresponds to the property/attribute on the object (column in database-speak). This can also extend to other objects using the `__` string to reach across a relationship and even evaluate content: `Server.objects.filter(environment__name__startswith='S')`. This returns all Servers in an Environment whose name starts with 'S'.

This is the tip of the iceberg for filtering objects in Django ORM. You're strongly encouraged to review the Django ORM documentation at: https://docs.djangoproject.com/en/3.2/topics/db/models.

### Other Queryset Methods
Some usesful additional Queryset methods include:

* count()
  * Returns the count of objects in a queryset: `Server.objects.count()` or `Server.objects.filter(status='ACTIVE').count()`
* get()
  * Returns ONE record matching the expression passed: `Server.objects.get(id=555)`. If more than one Model is returned, an error is thrown.
* get_or_create()
  * Retrieves an object matching the passed parameter values or creates a new one.
*

### Q Objects
Filters are nice for simple queries, but can get unwieldy with a more complicated query is needed. To solve this issue Q objects were introduced to express conditions as functions against with boolean logic can be run. Building on the examples above, we could combine filters to return all Servers that are ACTIVE AND whose Environment name begins with the letter 'S' with the expression:

`servers = Server.objects.filter(status='ACTIVE', environment__name__startswith='S')`

Nice, but what if we want to take the Union/OR of these two conditions meaning we want to return all Servers who are active OR are in an environment whose name starts with 'S'. Somewhat of a contrived example, but a great use-case for using a Q object:

`servers = Server.objects.filter(Q(status='ACTIVE') | Q(environment__name__startswith='S'))`

Can you spot the difference? Rather than supplying a list of parameters, one for each condition, we use the `|` operator to OR these conditions and pass as a single parameter to the filter method.

