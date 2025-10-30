from django.urls import path, re_path
from school_app import views
from django.conf import settings
from django.views.static import serve
urlpatterns = [
    path('', views.PostListView, name="main_page"),
    path('month/', views.PostByMonthView, name="month_filter"),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]