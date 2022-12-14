from django.views.generic import TemplateView
from django.conf import settings


class IndexView(TemplateView):
    template_name = "app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Django with Dynaconf - Version ' + settings.VERSION
        context['message'] = 'Our SECRET_KEY is ' + settings.SECRET_KEY
        context['db_user'] = 'Our database user is ' + settings.DATABASES.default.USER
        return context
