from .views import index, pricing
from django.urls import path


urlpatterns = [
    path('', index, name="index"),
    path('prices', pricing, name="pricing"),
]