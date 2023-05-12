from django.contrib import admin
from django.urls import path
from user import views as uv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', uv.main_text),
]
