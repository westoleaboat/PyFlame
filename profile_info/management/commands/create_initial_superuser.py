# from django.core.management.base import BaseCommand
# from django.contrib.auth import get_user_model

# class Command(BaseCommand):
#     help = 'Create the initial superuser if it does not exist.'

#     def handle(self, *args, **options):
#         User = get_user_model()
#         if not User.objects.filter(username='admin').exists():
#             User.objects.create_superuser('admin', 'admin@pyflame.com', '111')
#             self.stdout.write(self.style.SUCCESS('Superuser "admin" created.'))
#         else:
#             self.stdout.write(self.style.SUCCESS('Superuser "admin" already exists.'))
