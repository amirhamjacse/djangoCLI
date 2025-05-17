from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # we can write logic here also call other method
        print('Working it is')
        self.something()
        self.moremethod()
        # name = kwargs['name']
        # self.stdout.write(f"Hello, {name}!")
    
    def something(self):
        print('wroking the something mehtod')
    
    def moremethod(self):
        print("more method")
