from django.contrib import admin
from django.urls import path

from myapp import views as myapp_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp_views.index, name='index'), 
    path('tags/<slug:slug>/', myapp_views.tags, name='tags'),
]
