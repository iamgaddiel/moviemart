from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView



class IndexPage(TemplateView):
    template_name = "core/index.html"