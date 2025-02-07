
from django.urls import path
from . views import homeView,article_list,article_detail,contact,about
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", homeView, name="home"),
    path('article_list/', article_list, name='article_list'),
    path('<int:article_id>/', article_detail, name='article_detail'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)