from django.urls import include, path

urlpatterns = [
    # Other URL patterns for the project...
    path('', include('app.urls', namespace='app')),
]
