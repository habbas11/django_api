from django.core.management.base import BaseCommand, no_translations
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Waiting for DB...')
        db_up = False

        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except(OperationalError, Psycopg2OpError):
                self.stdout.write('Database unavailable, waiting for 1 sec...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is available!'))
