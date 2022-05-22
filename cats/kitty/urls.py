from django.urls import path

from . import views
app_name = 'cats'

urlpatterns = [
    path('', views.index, name='cats_main'),
    path('cat/<slug:cat_slug>/', views.detail, name='cat'),
]
