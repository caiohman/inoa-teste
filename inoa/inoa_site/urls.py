from django.urls import path

from . import views

app_name = 'inoa_site'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:validate>/', views.validate_login, name='validate_login'),
    path('<int:user_id>/home/', views.home, name='home')
]
