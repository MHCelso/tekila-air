# from django.shortcuts import render
# from django.views import View
from django.views.generic import TemplateView

# class IndexView(View):
#	def get(self, request, *args, **kwargs):
#		return render(request, 'base.

class IndexView(TemplateView):
    template_name = "base.html"