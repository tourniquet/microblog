from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'post'
urlpatterns = [
  path('', views.index, name='index'),
  path('post/<int:post_id>/', views.post, name='post'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
