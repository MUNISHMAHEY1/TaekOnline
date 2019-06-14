from django.apps import AppConfig

class TaekOnlineConfig(AppConfig):
    name = 'taekonline'
    verbose_name = 'TaekOnline'

    def ready(self):
        import taekonline.signals