from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'scripts to deal with old data to new version'
    functions = []
    def add_arguments(self, parser):
        pass
        #parser.add_argument('update', nargs='+', type=int)

    def handle(self, *args, **options):
        from sca.tasks import refresh_all_asset_data
        refresh_all_asset_data()
        self.stdout.write(
            self.style.SUCCESS('Successfully flash old data  "%s"' %
                               '123123213321'))