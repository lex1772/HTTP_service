from django.urls import path

from files.apps import FilesConfig
from files.views import UploadCreateView, UploadListView, UploadDetailView, UploadDeleteView

app_name = FilesConfig.name
urlpatterns = [
    path('upload/', UploadCreateView.as_view(template_name='files/upload_form.html'), name='upload'),
    path('', UploadListView.as_view(template_name='files/upload_list.html'), name='upload_list'),
    path('<int:pk>/', UploadDetailView.as_view(template_name='files/upload_detail.html'), name='upload_detail'),
    path('delete/<int:pk>/', UploadDeleteView.as_view(), name='upload_delete'),
]