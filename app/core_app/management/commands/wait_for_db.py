import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until the db is active """

    def handle(self, *args, **options):
        self.stdout.write('#--------WAITING FOR DATABASE--------#')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable. Waiting for 1 sec....')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('** DATABASE AVAILABLE **'))
