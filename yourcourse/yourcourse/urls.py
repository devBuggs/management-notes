from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

# favicon view of the web server
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('favicon.ico', favicon_view),
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('course/', include('courseapp.urls')),
    path('', include('payments.urls')),
    path('interview/', include('interviewapp.urls')),
    path('', include('blog.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
