from django.conf.urls import url
from register_app.views import signup, register


urlpatterns = [
    url(r'^$', signup),
    url(r'^test/$', register, name='register'),
]