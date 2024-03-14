# urls.py (in your project directory)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('price_comparison_app.urls')),  # Replace 'your_app' with the name of your Django app
]
