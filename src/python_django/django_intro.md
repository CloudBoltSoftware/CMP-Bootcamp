# Introduction to Django

Django is a open-source Web-application framework that facilitates that facilitates the rapid development of web-based applications. This framework is flexible enough to accommodate past, current, and future trends in web-app architecture, including: MVC, Ajax, API-first, and micro-services.

THis is a batteries-included framework that works to embed best practices in security, application structure, and scalability. The term "batteries-included" refers to the fact that Django includes support for the most common tasks and scenarios at first deployment without relying on a lot third-party libraries.

Since Django serves as the application framework for CMP, it's strongly recommended that you review their great documentation at https://docs.djangoproject.com/. Understanding Django is essential for understanding the machinery on which the CMP application is delivered.

## MVC (MVT) Application Framework
The MVT (model-view-template) framework in Django provides developers with a way to separate data-access and manipulation, its preparation, and its display. Django arranges system components as "applications". These applications contain database models (see more on ORM), python-based views, and html templates. Database models are typically defined in a file called `models.py`, views in `views.py`, and html templates in a `templates` folder.

Applications namespaces correspond to Python module name spaces. For instance the "AWS Resource Handler" application is stored at `resourcehandlers.aws`. In this case, the name of the Django application is simply `resourcehandlers.aws`. Looking at the source code under `src/` you'll see each unique resource handler has its own application defined under `src/resourcehandlers/`. 

When an inbound request is received, it is processed by a view function defined in an application's `view.py` file and mapped to a a specific URL in `urls.py`. 

For example, let's say I have a Django application called `my_app`. I may have a view function defined in `my_app/views.py` called `my_view_fn`. This function is mapped in `my_app/urls.py` to the URL path `/my_view`. When Django receives a request for `/my_view`, it executes the `my_view_fn` passing the HTTP request. The `my_view_fn` might fetch data from a database, and pass it to an HTML template at `my_app/templates/my_view.html` to be rendered to the requesting browser.

In addition to `models.py`, `views.py`, `urls.py`, another common file is `forms.py` which is used to defined forms that collect and process information submitted by users via POST actions. Keep in mind that these file names are Django convention -- models, view functions, and forms can be declared in any Django module.

* Model = `models.py`
* View = `views.py`, `forms.py`
    * via `urls.py`
* Template = `templates/*`
    * via function in `views.py`

Django is made aware of "applications" by including the application name the list called `INSTALLED_APPS` as defined in `settings.py`

## Object-Relational Mapping (ORM)

Object-Relational Mappers (ORMs) are frameworks that allow programmers to access database data through the syntax and semantics of a given programming language. The alternative to using an ORM to access database data is to specify SQL commands that return datasets that must be manually parsed and iterated. Rather than querying for a list of users with a SQL statement such as `SELECT * FROM Users WHERE Status='ACTIVE'` an ORM allows a developer to query using the current language without a context-shift to SQL: `User.objects.filter(Status='ACTIVE')`. 

The SQL statement in the example above will often return a tabular list of rows whose columns correspond to User attributes. The result return by the ORM is a list of user-defined User objects as defined by the programming language. Columns in the database are automatically converted to the appropriate formats and are mapped to properties on the User Object.

This capability allows the user to focus on the object model as defined by the application without having to do the mental mapping between database tables and tabular datasets. With Django ORM, printing a list of usernames can be done without writing a line of SQL.

```
users = User.objects.filter(active=True)
for user in users:
    print(user.username)
```

What's more, because writing the actual SQL is left to the framework, there's a level of abstraction between the programming language and the underlying database. This is how CloudBolt CMP is able to support PosgreSQL and MySQL database backends simply by changing the datasource connection.

## Django REST Framework (DRF)

Modern web-applications make heavy use of APIs called directly from the browser rather than the MVC pattern common in the past. While each approach has it's pros and cons, API-first architecture as well as the programmable web have both contributed to the need for a comprehensive framework that allows Django to provide API services. 

At its core, the Django REST framework integrates authentication, autogenerated endpoint documentation, and object serialization for Python data types in a single package. This functionality works together with the Django ORM to simplify the process of working with database data via a browsable API in JSON format.

More information about Django REST Framework is available at: https://www.django-rest-framework.org. 




 