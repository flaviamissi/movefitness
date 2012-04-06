from django.views.generic import DetailView

from content.models import Content


class ContentView(DetailView):
    model = Content

    def get_template_names(self):
        return ["%s.html" % self.object.slug]
