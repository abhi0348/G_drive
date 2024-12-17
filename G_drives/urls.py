from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('/', views.home, name='home'),
    path('folders/', views.folder_list, name='folder_list'),
    path('folders/create/', views.create_folder, name='create_folder'),
    path('folders/edit/<int:pk>/', views.update_folder, name='update_folder'),
    path('folders/delete/<int:pk>/', views.delete_folder, name='delete_folder'),
    path('folders/<int:folder_id>/upload/', views.upload_file, name='upload_file'),
    path('folders/<int:folder_id>/', views.folder_details, name='folder_details'), 


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)