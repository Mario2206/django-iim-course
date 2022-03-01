from django.urls import path 
from . import views 

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.get, name='get'),
    path('buy/<int:id>', views.buy, name='buy')
]