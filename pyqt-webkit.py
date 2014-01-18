import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *
import re
import subprocess


# Start the Django server
#manage_path = local_settings.root_dir + 'manage.py'
manage_path = 'onweb/manage.py'
server = subprocess.Popen(["python", manage_path, "runserver"])

app = QApplication(sys.argv)
web = QWebView()
web.load(QUrl("http://127.0.0.1:8000/"))
web.show()
sys.exit(app.exec_())

