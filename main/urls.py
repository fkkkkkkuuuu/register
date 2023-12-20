from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('news/', include('news.urls')),
    path('products/', include('products.urls')),
    path('home/', include('home.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
