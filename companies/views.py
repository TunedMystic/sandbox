from django.shortcuts import render

from .models import Company


def company_list(request):
    companies = Company.objects.all()
    return render(request, 'companies/company-list.html', {
        'companies': companies
    })
