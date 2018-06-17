from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/', include('app_tienda.api.urls', namespace='api')),
]
