from django.apps import AppConfig


class FetchNewsConfig(AppConfig):
    name = 'fetch_news'
    verbose_name = "News"

    def ready(self):
        import fetch_news.signals
