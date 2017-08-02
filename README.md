# Catalog Project

This python web app allows for CRUD operations on a SQLite database.  Users can login using Google+ or Facebook.  Users are only allowed to edit and/or delete category items that they created.

## Getting Started

You can download/fork my repository for this project at https://github.com/stevenyoung131/catalog-project

You will need to set up a vagrant linux virtual machine to run this code.  Instructions at https://www.vagrantup.com/intro/getting-started/

Once the virtual environment is set up and running and the repository is forked into the virual machine's shared folder,
run project.py to begin serving the web app at localhost:5000.
(If you prefer to create your own categories and items, simply delete the catalog.db file and run db_setup.py to create an empty
database.  To enable the link to create new categories, uncomment line 8 of 'home.html')

## Accessing API endpoints

There are several API endpoints that generate JSON objects.

* Full catalog can be viewed at ./catalog.json
* Categories can be viewed at ./catalog/<category>.json
* Individual items can be viewed at ./catalog/<category>/<item>.json

## Built With

* [Flask](flask.pocoo.org/) - Template and python implementation
* [SQLAlchemy](https://www.sqlalchemy.org/) - SQL Crud Operations
* [Bootstrap](getbootstrap.com/) - The web framework used

## Versioning

I use [SourceTree](https://www.sourcetreeapp.com/) for version control.

## Authors

* **Steven Young** - *Initial work* - (https://github.com/stevenyoung131)