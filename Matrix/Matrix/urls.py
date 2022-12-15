from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', include('appmatrix.urls')),
    path('api/', include('API_matrix.urls')),
]