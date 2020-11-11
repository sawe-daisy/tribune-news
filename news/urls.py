from django.conf.urls import url
from django.conf.urls.static import static
from django.conf.urls.static import settings
from . import views
from django.urls import path, re_path

urlpatterns=[
    path('', views.news_today, name='newsToday'),
    re_path('archives/(\d{4}-\d{2}-\d{2})/',views.past_days_news,name = 'pastNews'),
    path('search/', views.searchResults, name='searchResults')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)