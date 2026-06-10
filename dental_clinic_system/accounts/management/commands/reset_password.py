"""
Management command to reset user password
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Reset password for a specific user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the user')
        parser.add_argument(
            '--password',
            type=str,
            default='temp123456',
            help='New password (default: temp123456)'
        )

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        
        try:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully reset password for user "{username}"'
                )
            )
            self.stdout.write(f'New password: {password}')
            
        except User.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'User "{username}" does not exist')
            )
            # List available users
            users = User.objects.all().values_list('username', flat=True)[:10]
            self.stdout.write('Available users:')
            for u in users:
                self.stdout.write(f'  - {u}')
