from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='api')),
    path('api', views.play, name='api'),
]