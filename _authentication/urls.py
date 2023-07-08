from django.urls import path


from .views import (
    Registration
)


app_name  = 'authentication'


urlpatterns = [
    path('', Registration, name='register'),
]