from django.urls import path
from .views import PostCreateArticle, PostUpdate, PostDelete


urlpatterns = [
   path('create/', PostCreateArticle.as_view(), name='apost_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='apost_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='apost_delete'),
]