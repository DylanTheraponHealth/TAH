from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Member
from django.template import loader

# Create your views here.
def members(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def diabetes(request):
    template = loader.get_template('diabetes.html')
    labels = []
    data = []

    queryset = Member.objects.order_by('-lastname')[:5]
    for name in queryset:
        labels.append(name.firstname)
        data.append(name.num_users)

    return HttpResponse(template.render({        
        'labels':labels,
        'data':data,}))

def pie_chart(request):
    labels = []
    data = []

    queryset = Member.objects.order_by('-lastname')[:5]
    for name in queryset:
        labels.append(name.firstname)
        data.append(name.num_users)

    return render(request, "charts/chart.html",{
        'labels':labels,
        'data':data,
    })