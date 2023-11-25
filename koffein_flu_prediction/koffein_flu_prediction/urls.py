from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
	path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]
