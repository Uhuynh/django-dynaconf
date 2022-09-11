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

# 2. Dynaconf - Django Extension
- [Dynaconf extensions for Django](https://www.dynaconf.com/django/) works by patching the `settings.py` file 
with dynaconf loading hooks
- The change is done on a single file and then in your whole project every time you call `django.conf.settings`
you will have access to dynaconf attributes and methods.
- Instead of defining all of our project settings / variables in Django default `settings.py`:
  ````python
  # settings.py
  ...
  SEVRER='foo.com'
  FOO='bar'
  ...
  ````
  With Dynaconf, we can easily define the variables in `settings.{yaml, toml, ini, json, py}`, which can change
based on the environments, for example `[default]`, `[development]`, and `[production]`
  ````yaml
  # settings.yaml
  
  default:
    server: foo.com
    foo: bar
  
  development:
    server: devserver.com
    foo: bar dev
    
  production:
    server: prodserver.com
    foo: bar prod
  ````
# 3. Setup
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

# 4. Clean up
To clean up your environment (containers, volumes) run:
```shell
$ docker-compose down --volumes --remove-orphans
$ docker system prune
```
**Notes**:
- this will purge your volumes and all data

