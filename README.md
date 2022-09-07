# django-dynaconf
A simple Django app with Dynaconf integrated. The setup is based on Docker Compose.

# 1. What is Dynaconf?
- [Dynaconf](https://www.dynaconf.com/) is a layered configuration system for Python applications - with strong 
support for [12-factor applications](https://12factor.net/config) and extensions for Flask and Django.
- Some advantages of using Dynaconf:
  - Strict separation of settings from code
  - Store parameters in multiple file formats (.toml, .json, .yaml, .ini and .py)
  - Layered **[environment]** system.
  - Environment variables can be used to override parameters.
  - Support for `.env` files to automate the export of environment variables.
  - Drop in extension for Django `conf.settings` object.
  - Powerful `$ dynaconf CLI` to help you manage your settings via console.
## 1.1. Django Extension
- [Dynaconf extensions for Django](https://www.dynaconf.com/django/) works by patching the `settings.py` file 
with dynaconf loading hooks
- the change is done on a single file and then in your whole project every time you call `django.conf.settings`
you will have access to dynaconf attributes and methods.
# 2. Setup
- Make sure to install `Docker` and `Docker Compose` on the machine
    ```bash
    $ docker --version
    Docker version 20.10.8, build 3967b7d
    $ docker-compose --version
    docker-compose version 1.29.2, build 5becea4c
    ```
- Clone the repository: https://github.com/Uhuynh/django-dynaconf
- Run `$ docker-compose up -d`
- To verify the setup, go to `http://localhost:33000`

# 3. Clean up
To clean up your environment (containers, volumes) run:
```shell
$ docker-compose down --volumes --remove-orphans
$ docker system prune
```
**Notes**:
- this will purge your volumes and all data

