import os
import sys
import subprocess

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
    subprocess.call(['python', 'manage.py', 'runserver'])