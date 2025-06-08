from django.core.management.base import BaseCommand
from jobs.factories import JobFactory


class Command(BaseCommand):
    help = 'Seed job data using factory'

    def add_arguments(self, parser):
        parser.add_argument('--total', type=int, default=10,
                            help='Number of companies to create')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for _ in range(total):
            JobFactory()
        self.stdout.write(self.style.SUCCESS(
            f'Successfully created {total} fake jobs.'))
