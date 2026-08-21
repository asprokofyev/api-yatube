from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import GroupViewSet, PostViewSet, CommentViewSet

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='post-comments'
)

urlpatterns = [
    path('v1/api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('v1/', include(v1_router.urls)),
]
