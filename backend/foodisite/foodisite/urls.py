from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', include('login.urls')),
    path('login/', include('signup.urls')),
]
