from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router_v1 = SimpleRouter()
router_v1.register("posts", PostViewSet)
router_v1.register("groups", GroupViewSet)
router_v1.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment',
)
router_v1.register("follow", FollowViewSet)

urlpatterns = [
    path("v1/api-token-auth/", views.obtain_auth_token),
    path("v1/", include(router_v1.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
