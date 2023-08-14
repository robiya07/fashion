from django.urls import path

from main.views import HomeView, CreteContactView, AboutView

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', CreteContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
]
