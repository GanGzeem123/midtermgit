from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('go_login',views.login),
    path('request',views.request),
    path('reportrequest',views.reportrequest),

]