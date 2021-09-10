from django.views.generic import TemplateView

class HulkView(TemplateView):
    template_name = 'hulk.html'
    def get_context_data(self, **kwargs):
        return {
            'title': 'My About Page', 
            'body': 'Once upon a time ...',
        }

class IronManView(TemplateView):
    template_name = "iron_man.html"
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'My Home Page', 
            'body': 'This page is boring ...',
        }

class BlackWidowView(TemplateView):
    template_name = "black_widow.html"
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'My Home Page', 
            'body': 'This page is boring ...',
        }

class HerosView(TemplateView):
    template_name = "hero.html"

class IndexView(TemplateView):
    template_name = "index.html"

class RandomView(TemplateView):
    template_name = "random.html"