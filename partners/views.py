from django.views.generic import ListView

from content.models import Content
from move_fitness.views import BaseView
from partners.models import Partner


class PartnersView(BaseView, ListView):

    template_name = "partners.html"

    def get_context_data(self, *args, **kwargs):
        context = ListView.get_context_data(self, *args, **kwargs)
        context.update(BaseView.get_context_data(self, *args, **kwargs))
        context["partners"] = Partner.objects.all()

        content = Content.objects.filter(slug="parceiros")
        if content.exists():
            context["content"] = content[0]

        return context
