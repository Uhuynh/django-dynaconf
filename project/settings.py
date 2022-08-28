"""
https://docs.djangoproject.com/en/1.11/topics/settings/
https://docs.djangoproject.com/en/1.11/ref/settings/
https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#
# HERE STARTS DYNACONF EXTENSION LOAD
#

import dynaconf  # noqa
from dynaconf import Validator # noqa

settings = dynaconf.DjangoDynaconf(
    __name__,
    settings_files=[
        'settings.yaml'
    ],
    env_switcher='DJANGO_ENVIRONMENT',
    load_dotenv=True,
    validators=[
        Validator('ENVIRONMENT', must_exist=True),

        Validator('DEBUG', is_type_of=bool),
        Validator('ENVIRONMENT', is_in=('dev', 'pytest')),

    ]
)  # noqa

#
# HERE ENDS DYNACONF EXTENSION LOAD (No more code below this line)
#


