from django.conf.urls import url, include
from django.contrib import admin
from ServiceOrdering.views import login_user
urlpatterns = [
    url(r'^$', login_user),
    url(r'^admin/', admin.site.urls),
    url(r'services/', include('ServiceOrdering.urls'))
]
