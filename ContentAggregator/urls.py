from django.contrib import admin
from django.urls import path
from contents.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
        path('', home,name='home'),
    path('updatepython/', updatepython,name='updatepython'),
    path('updateprog/', updateprog,name='updateprog'),
    path('updatecovid/', updatecovid,name='updatecovid'),
    path('updatehiring/', updatehiring,name='updatehiring'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
