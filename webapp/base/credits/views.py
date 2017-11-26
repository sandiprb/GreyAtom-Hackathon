# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict
from .models import CustomerData

# Create your views here.
def index(request):
    return render(request, 'base.html', {})


def select_customer(request):
    context = {}
    cust_ids = CustomerData.objects.all()
    cust_ids = [q.custmer_id for q in cust_ids]
    context['customer_ids'] = cust_ids
    return render(request, 'form1.html', context)


def show_customer_data(request):
    context = {}
    if request.method == 'POST':
        cust_id = request.POST['customer_id']
        data = CustomerData.objects.get(custmer_id=cust_id)
        try:
            context['data'] = model_to_dict(data)
            return render(request, 'customer_data.html', context)
        except CustomerData.DoesNotExist:
            return HttpResponseRedirect('/select-customer/')


    return HttpResponseRedirect('/select-customer/')