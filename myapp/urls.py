from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('<id>', show_candidate, name="candidate"),
]
