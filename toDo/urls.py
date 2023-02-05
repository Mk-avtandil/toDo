from django.urls import path

from .views import Home, PostDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post_detail/<slug:post_slug>/', PostDetail.as_view(), name='detail')
]
