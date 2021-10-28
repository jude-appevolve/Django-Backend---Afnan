#!/bin/bash

python manage.py collectstatic
sudo supervisorctl restart all