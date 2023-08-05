from django.urls import path

from main.views import HomeView

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
