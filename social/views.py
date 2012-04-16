from django.views.generic import ListView

from content.models import Content
from social.models import Social
from move_fitness.views import BaseView


class SocialView(BaseView, ListView):

    template_name = "social.html"

    def get_context_data(self, *args, **kwargs):
        context = ListView.get_context_data(self, *args, **kwargs)
        context.update(BaseView.get_context_data(self, *args, **kwargs))
        context["social"] = {}

        social = Social.objects.all()
        for obj in social:
            context["social"][obj.social_networking] = obj.profile

        news = Content.objects.filter(slug="noticias")
        if news.exists():
            context["content"] = news[0]

        return context
