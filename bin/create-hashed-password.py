#!/usr/bin/env python

import os
import django 
import sys
from django.contrib.auth.hashers import make_password

os.environ.setdefault("PYTHONPATH", ".")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()

# Replace 'yourpassword' with the password you want to hash
plain_password = sys.argv[1] if len(sys.argv) > 1 else 'password'

hashed = make_password(plain_password)

print("Plain password:", plain_password)
print("Hashed password:", hashed)