from django.urls import path
from .views import HomePageView, AboutPageView, NamePageView

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("about/", AboutPageView.as_view(), name='about'),
    path("name/", NamePageView.as_view(), name='name'),
]