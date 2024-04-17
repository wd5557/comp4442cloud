from django.urls import path
from .views import index, summary_page, choose_page, monitor_data, monitor_page



urlpatterns = [
    path('', index, name='index'),
    path('summary', summary_page, name='summary'),
    path('driver', choose_page, name='driver'),
    path('api/data', monitor_data, name='monitor_data'),
    path('monitor/<str:driverID>', monitor_page, name='monitor'),
]
