"""
Test custom Django managment commands.
"""
from unittest.mock import patch

from psycopg2 import OperationalError as psychopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

