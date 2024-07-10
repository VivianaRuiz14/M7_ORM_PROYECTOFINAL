from django.core.management.base import BaseCommand
from toc_toc.services import *
class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        #crear_user('1234567-8', 'Pedro', 'Picapiedras', 'ppiedra@gmail.com', '12345','12345','Av. Rocadura 45')
        
        editar_user('1234567-8', 'Pedro', 'Picapiedras', 'pedrop@gmail.com', '54321','Av. Piedradura 45')