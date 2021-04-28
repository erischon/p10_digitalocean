#!/bin/sh

export DJANGO_SETTINGS_MODULE="core.settings.production"
export SECRET_KEY="password123"
export DB_NAME="thesubstitute"
export DB_USER="erischon"
export DB_PASSWORD="Thes2021="

cd /home/erischon/p10_digitalocean/
/home/erischon/p10_digitalocean/venv/bin/python3 /home/erischon/p10_digitalocean/manage.py etl
