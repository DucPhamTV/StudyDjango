from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'api/users', views.UserViewSet, basename='user')
router.register(r'api/items', views.ItemViewSet, basename='item')
router.register(r'api/comment', views.CommentViewSet, basename='comment')
router.register(r'api/image', views.ImageViewSet, basename='image')

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>', views.ItemDetailView.as_view(), name='detail'),
    #path('api/', views.ItemViewSet.as_view(), name='item'),
    path(r'api2/', include(router.urls)),
    #path('<name>', views.ItemView.as_view(), name='item'),
    path('api-auth/', include('rest_framework.urls')),
]
