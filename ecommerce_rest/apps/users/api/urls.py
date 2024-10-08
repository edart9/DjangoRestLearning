from django.urls import path
from apps.users.api.views import user_api_view,user_datail_api_view

urlpatterns = [
    path('usuario/',user_api_view, name='usuario-api'),
    path('usuario/<int:pk>',user_datail_api_view,name='usuario-datail-api-view')
]