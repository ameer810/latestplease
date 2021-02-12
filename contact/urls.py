from django.urls import include, path

from . import views
from . import api
app_name='contact'

urlpatterns = [
    path('',views.send_message , name='contact'),
    path('api',api.job_list_api , name='api'),
]