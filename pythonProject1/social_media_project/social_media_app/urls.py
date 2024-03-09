from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('social_media_app.urls')),  # Example: replace 'your_app' with your app's name
    path('logout/', include('social_media_app.urls')),
    path('register/', include('social_media_app.urls')),
    path('home/', include('social_media_app.urls')),
    path('accounts/', include('social_media_app.urls')),
    # Add a pattern for the root path
    path('', include('social_media_app.urls')),
]
