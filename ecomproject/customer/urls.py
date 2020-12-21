from django.urls import path
from . import views


from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.home, name='customer-home'),
    path('getstarted/', views.getstarted, name='customer-getstarted'),
    path('login/', views.logIn, name='customer-login'),
    path('logout/', views.logOut, name='customer-logout'),
    path('user_profile/<int:pk>',views.userProfile, name='customer-profile')
]


if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 