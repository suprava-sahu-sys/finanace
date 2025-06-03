import unittest
import os
from backup_restore import backup_database, restore_database

class TestBackupRestore(unittest.TestCase):
    def test_backup_and_restore(self):
        backup_file = backup_database()
        self.assertIsNotNone(backup_file, "Backup path is None")
        self.assertTrue(os.path.exists(backup_file), "Backup file was not created")

        result = restore_database(backup_file)
        self.assertTrue(result, "Restore failed")


if __name__ == "__main__":
    unittest.main()
