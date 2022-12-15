from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from . import views

urlpatterns = [
    path('own/', views.MatrixVectorView.as_view(), name='c_vec'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularAPIView.as_view(), name='home'),
    path(
        'docs/',
        SpectacularSwaggerView.as_view(
            url_name='schema'
        ),
        name='swagger-ui',
    ),
]
