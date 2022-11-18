from django.contrib import admin
from django.urls import path

from myapp import views as myapp_views # < here
urlpatterns = [
    path('admin/', admin.site.urls),
    path('flower/<slug:slug>/', myapp_views.detail, name='detail'), 
    path('', myapp_views.index, name='index'), # < here
]
