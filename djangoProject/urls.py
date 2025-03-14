from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # Local apps
    path("accounts/", include("accounts.urls")),
    path("", include("pages.urls")),
    path("books/", include("books.urls")),
]
