from PySide import QtGui, QtCore, QtWebKit
from unipath import Path


class Preview(QtWebKit.QWebView):
	def __init__(self, parent=None):
		super(Preview, self).__init__(parent)
		
	def load_html(self, path):
		self.load(QtCore.QUrl.fromLocalFile(path))