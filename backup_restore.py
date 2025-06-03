import shutil
import os
from datetime import datetime

DB_FILE = 'finance_app.db'  # update this if your DB filename differs

def backup_database():
    src = 'finance_app.db'
    if not os.path.exists(src):
        print("❌ Database file not found.")
        return False

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = f"finance_app_backup_{timestamp}.db"

    try:
        shutil.copy(src, dest)
        print(f"✅ Backup successful: {dest}")
        return dest
    except Exception as e:
        print(f"❌ Backup failed: {e}")
        return False

def restore_database(backup_file):
    if os.path.exists(backup_file):
        shutil.copyfile(backup_file, DB_FILE)
        print(f"✅ Database restored from {backup_file}")
        return True
    else:
        print(f"❌ Backup file {backup_file} not found!")
        return False
