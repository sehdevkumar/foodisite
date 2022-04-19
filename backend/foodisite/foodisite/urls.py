from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', include('login.urls')),
    path('signup/', include('signup.urls')),
]
