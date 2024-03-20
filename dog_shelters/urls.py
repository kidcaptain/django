
from django.urls import path
from . import views

app_name = 'dog_shelters'

urlpatterns = [
    path('classes/<int:pk>', views.index, name='index'),
    path('', views.classe_list, name='classe_list'),
    path('classe/<int:pk>', views.classe_detail, name='classe_detail'),
    # path('classes/<int:pk>', views.classe_delete, name='classe_delete')
]