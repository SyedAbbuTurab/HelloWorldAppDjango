from django.urls import path, include
from .views import hello_world, hello_world_html

urlpatterns = [
    path('hello/', hello_world, name='hello_world_json'),
    path('hellohtml/', hello_world_html, name='hello_world_html'),
]
