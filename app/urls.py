from django.urls import path
from .views import home, about, index

app_name = "app"

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('index/', index, name='index'),
]
