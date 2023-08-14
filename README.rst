=======================================
Django API Data Cache
=======================================

API Data Cache is a simple mixin for Django REST framework to serve database
objects to clients using the api-data-cache service.

It is composed of a mixing for list views that processes the request parameters from api-data-cache 
clients for pagination and filtering.


Installation
------------

1. Install the package using pip:

   .. code-block:: bash

       pip install django-data-retrieval-mixin

2. Add `'api-data-cache'` to your Django project's `INSTALLED_APPS` list in the `settings.py` file:

   .. code-block:: python

       INSTALLED_APPS = [
           # ...
           'rest_framework',
           'api-data-cache',
           # ...
       ]



Usage
-----

1. Import the `APIDataCacheListViewMixin` into your view module:

   .. code-block:: python

       from api-data-cache.mixins import APIDataCacheListViewMixin

2. Inherit the `APIDataCacheListViewMixin` in your view class:

   .. code-block:: python

       from api-data-cache.mixins import APIDataCacheListViewMixin
       from rest_framework import viewsets
       from .models import YourModel
       from .serializer import YourPartialSerializer


       class YourListView(APIDataCacheListViewMixin, viewsets.GenericViewSet):
           queryset = YourModel.objects.all()
           serializer_class = YourPartialSerializer
           search_fields = ['field1', 'field2']


