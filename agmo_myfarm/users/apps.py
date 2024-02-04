from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "agmo_myfarm.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import agmo_myfarm.users.signals  # noqa: F401
        except ImportError:
            pass
