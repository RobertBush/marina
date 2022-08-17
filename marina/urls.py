from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from power import views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path(
        "boats/", views.BoatViewSet.as_view(actions={"get": "list", "post": "create"})
    ),
    path(
        "boats/<int:pk>/",
        views.BoatViewSet.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
                "patch": "partial_update",
            }
        ),
    ),
    path(
        "engines/",
        views.EngineViewSet.as_view(actions={"get": "list", "post": "create"}),
    ),
    path(
        "engines/<int:pk>/",
        views.EngineViewSet.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
                "patch": "partial_update",
            }
        ),
    ),
    path(
        "boatengines/",
        views.BoatEngineViewSet.as_view(actions={"get": "list", "post": "create"}),
    ),
    path(
        "boatengines/<int:pk>/",
        views.BoatEngineViewSet.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
                "patch": "partial_update",
            }
        ),
    ),
    path("admin/", admin.site.urls),
]
urlpatterns = format_suffix_patterns(urlpatterns)
