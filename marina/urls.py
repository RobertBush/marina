from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from power import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('boats/', views.BoatList.as_view()),
    path('boats/<int:pk>/', views.BoatDetail.as_view()),
    path('engines/', views.EngineList.as_view()),
    path('engines/<int:pk>/', views.EngineDetail.as_view()),
    path('boatengines/', views.BoatEngineList.as_view()),
    path('boatengines/<int:pk>/', views.BoatEngineDetail.as_view()),
    path('admin/', admin.site.urls),
]
urlpatterns = format_suffix_patterns(urlpatterns)
