from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^company/', views.company_list, name='company-list'),
]
