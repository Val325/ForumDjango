from django.contrib import admin
from django.urls import path, re_path
from myProject import views
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.MainText, name='upload_image'),
    path('reg/', views.sign_up),
    path('login/', views.sign_in),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('posts/<id>', views.Posts),
    path('add/', views.add_article),
    path('category/<id>', views.category),
    path('admin/', admin.site.urls),
    re_path(r'^profile/', views.profile),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)