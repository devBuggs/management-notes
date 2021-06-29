from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    # it just imports the signal file when the app is ready
    def ready(self):
        import accounts.signals