from django.urls import path, include
from .views import PropertyPostView, PropertyListView, PropertyDeleteView, PropertyEditView, PropertyDetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('post', PropertyPostView.as_view(), name='listing'),
    path('view_properties', PropertyListView.as_view(), name='view_properties'),
    path('post/<int:pk>/delete/', PropertyDeleteView.as_view(), name='delete-post'),
    path('edit/<int:pk>/update/', PropertyEditView.as_view(), name='update-post'),
    path('detail/<int:pk>/property-detail/', PropertyDetailView.as_view(), name='property-detail'),    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)