=======================================
Simple Django Server
=======================================

Serve the table Measurement; list, advanced-list and retrive operations.

Usage
------------

1. Install the package using pip:

   .. code-block:: bash

       pip install -r requirements.txt
       python manage.py migrate
       python manage.py runserver 9000

2. Get the using the endpoints:  
    * List: `/measurements/`
    * Advanced list : `/measurements/filtered/`
    * Retrieve : `/measurements/{id}/`


You can visualize the results in a front-end by running the api_data_cache angular demo at 
https://github.com/cviolbarbosa/api_data_cache/tree/main/demo.

   .. code-block:: bash

        npm start