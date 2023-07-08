from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registeration', include('_authentication.urls'))
    # path('auth/', include('_authentication.urls'))
]

# STatic and Media Files
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

