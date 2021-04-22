from django.core.management.base import BaseCommand

from database.utils import DBManage  # Can be remove if we don't want to delete
from database.extract import Extract
from database.transform import Transform
from database.load import Load


class Command(BaseCommand):
    '''
    I launch the ETL
    '''

    def handle(self, *args, **kwargs):
        self.stdout.write('Launching the ETL :')
        managing = DBManage()  # Can be remove if we don't want to delete
        managing.delete_tables()  # Can be remove if we don't want to delete
        self.stdout.write('Start by Extracting...')
        extract = Extract()
        extract.extract()
        self.stdout.write('Now Transforming...')
        transform = Transform()
        transform.transform_basic()
        self.stdout.write('And finaly Loading...')
        loading = Load()
        loading.load_data()
