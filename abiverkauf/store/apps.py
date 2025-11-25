from django.apps import AppConfig

class StoreConfig(AppConfig):
    name = 'abiverkauf.store'

    def ready(self):
        import store.signals  # noqa
