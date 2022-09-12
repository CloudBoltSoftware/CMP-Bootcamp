# Introduction to Django

Django is a open-source Web-application framework that facilitates that facilitates the rapid development of web-based applications. This framework is flexible enough to accommodate past, current, and future trends in web-app architecture, including: MVC, Ajax, API-first, and micro-services.

THis is a batteries-included framework that works to embed best practices in security, application structure, and scalability. The term "batteries-included" refers to the fact that Django includes support for the most common tasks and scenarios at first deployment without relying on a lot third-party libraries.

Since Django serves as the application framework for CMP, it's strongly recommended that you review their great documentation at https://docs.djangoproject.com/. Understanding Django is essential for understanding the machinery on which the CMP application is delivered.

## MVC (MVT) Application Framework
The MVT (model-view-template) framework in Django provides developers with a way to separate data-access and manipulation, its preparation, and its display. Django arranges system components as "applications". These applications contain database models (see more on ORM), python-based views, and html templates. Database models are typically defined in a file called `models.py`, views in `views.py`, and html templates in a `templates` folder.

Applications namespaces correspond to Python module name spaces. For instance the "AWS Resource Handler" application is stored at `resourcehandlers.aws`. In this case, the name of the Django application is simply `resourcehandlers.aws`. Looking at the source code under `src/` you'll see each unique resource handler has its own application defined under `src/resourcehandlers/`. 

When an inbound request is received, it is processed by a view function defined in an application's `view.py` file and mapped to a a specific URL in `urls.py`. 

For example, let's say I have a Django application called `my_app`. I may have a view function defined in `my_app/views.py` called `my_view_fn`. This function is mapped in `my_app/urls.py` to the URL path `/my_view`. When Django receives a request for `/my_view`, it executes the `my_view_fn` passing the HTTP request. The `my_view_fn` might fetch data from a database, and pass it to an HTML template at `my_app/templates/my_view.html` to be rendered to the requesting browser.

In addition to `models.py`, `views.py`, `urls.py`, another common file name is `forms.py` which is used to defined forms that collect and process information submitted by users via POST actions. 

* Model = `models.py`
* View = `views.py`, `forms.py`
    * via `urls.py`
* Template = `templates/*`
    * via function in `views.py`

Django is made aware of "applications" by including the application name the list called `INSTALLED_APPS` as defined in `settings.py`



## Object-Relational Mapping (ORM)

## Django Rest Framework


