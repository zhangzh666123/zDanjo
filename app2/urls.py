from django.urls import path
from app2 import views

urlpatterns = [
    path("app2/show/<int:id>/", views.show),
]
