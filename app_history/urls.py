from django.urls import path
from . import views
urlpatterns = [
    path('api/v1/gethistories/', views.UsersSearchHistory.as_view(), name='history')
]
