from django.urls import path

from main.views import HomeView, CreteContactView

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', CreteContactView.as_view(), name='contact'),
]
