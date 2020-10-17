from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

#router = DefaultRouter()
#router.register(r'api/users', views.UserViewSet, basename='user')
#router.register(r'api/items', views.ItemViewSet, basename='item')

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api/', views.ItemViewSet.as_view(), name='item'),
    #path('api', include(router.urls))
    #path('<name>', views.ItemView.as_view(), name='item'),
]
