import sys
import config
sys.path.insert(0, config.DOCUMENT_ROOT)

from app import app as application
