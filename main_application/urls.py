from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.render_calc),
    path('calculate/', views.calculate, name = "calculate"),
]