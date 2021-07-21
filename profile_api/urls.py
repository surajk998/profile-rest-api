from django.urls import path, include
from profile_api import views

from rest_framework import routers

router = routers.DefaultRouter()

router.register('profile', views.UserProfileViewSet)
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('feed', views.UserProfileFeedViewSet )


urlpatterns = [
  path('hello-view/', views.HelloApiView.as_view()),
  path('login/', views.UserLoginApiView.as_view()),
  path('',include(router.urls))
]