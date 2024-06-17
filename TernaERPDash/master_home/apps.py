from django.apps import AppConfig


class MasterHomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'master_home'

    # def ready(self):
    #     import master_home.signals
