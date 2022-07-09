from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:id>/', detail, name='detail'),
    path('new/', create, name='create'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('load/', load, name='load'),
    path('search/', search, name='search'),
]