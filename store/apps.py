from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'

    def ready(self):
        import os
        from django.contrib.auth import get_user_model

        def create_superuser():
            User = get_user_model()
            username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
            password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
            email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
            if username and password and not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, email=email, password=password)

        try:
            create_superuser()
        except Exception:
            pass