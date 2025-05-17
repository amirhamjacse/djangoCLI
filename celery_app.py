import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CONFIG.settings')

# Create a Celery app instance
app = Celery('CONFIG')

# Load configurations from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks in all Django apps
app.autodiscover_tasks()

# Workaround for Windows issues, setting the worker pool to 'solo'
app.conf.update(
    worker_pool='solo',  # Ensure it uses a single-threaded pool for Windows
)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
