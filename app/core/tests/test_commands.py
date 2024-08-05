"""
Test custom Django management commands
"""
# mock db
from unittest.mock import patch

# potential error we might get while connecting to db (postgre is not ready)
from psycopg2 import OperationalError as Psycopg2Error

# call the command for testing
from django.core.management import call_command
# another error might occur while connecting to db
# (django test db is not ready)
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch("core.management.commands.wait_for_db.Command.check")
class CommandTests(SimpleTestCase):
    """Test commands."""

    # patch_check is arg from @Command.check decorator
    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db if db ready."""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    # db is not yet ready
    # replace sleep time for efficiently executing test cases
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for db when getting OperationalError."""
        # raise Psycopg2Error (for postgre not ready) twice then raise 3
        # OperationlError (for python db not ready) then success
        patched_check.side_effect = [Psycopg2Error] * 2 + \
                                    [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
