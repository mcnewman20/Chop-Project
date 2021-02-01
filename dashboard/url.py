from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('dashboard/data', views.pivot_data, name='pivot_data'),
    path('', views.home_page, name='home'),
    path('use_a_sample', views.get_sample_code, name='use_a_sample')
]