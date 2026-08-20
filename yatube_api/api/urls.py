from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import GroupViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('', include(router.urls)),
    path(
        'posts/<int:post_id>/comments/',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='post-comments-list'
    ),
    path(
        'posts/<int:post_id>/comments/<int:pk>/',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='post-comments-detail'
    ),
]
