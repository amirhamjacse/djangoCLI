# from django.core.management.base import BaseCommand
# from datetime import datetime

# class Command(BaseCommand):
#     help = "Prints a message every 10 minutes"

#     def handle(self, *args, **kwargs):
#         now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         print(f"[{now}] This is a scheduled message from Django CLI.")


import time
from datetime import datetime
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Repeats a task every 30 seconds"

    def handle(self, *args, **kwargs):
        self.stdout.write("🔄 Starting 30-second loop... Press Ctrl+C to stop.")
        try:
            while True:
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"[{now}] ✅ Task is running...")

                # Place your actual logic here
                # Example: fetch data, process queue, check a flag, etc.

                time.sleep(2)  # Wait for 30 seconds before next run
        except KeyboardInterrupt:
            self.stdout.write("\n🛑 Stopped loop manually.")
