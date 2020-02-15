#!/usr/bin/python3
import sys, logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/antiviralvoyager/")

from antiviralvoyager import app as application
#application.secret_key = 0
