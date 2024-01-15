"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main import settings

admin.site.site_header = "Система банка"

urlpatterns = [
    # path('__debug__/', include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path("", include("reg_auf.urls")),
    path("", include("cards.urls")),
    path("", include("bank_account.urls")),
    path("", include("credit.urls")),
    path("", include("deposit.urls")),
    path("", include("history.urls")),

]
# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns = [
#                       path('__debug__/', include(debug_toolbar.urls)),
#                   ] + urlpatterns
#
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)