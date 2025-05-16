from django.urls import path

from core import views


urlpatterns = [
    path('', views.index, name='index'),    
    path('signup/', views.signup_view, name='signup'),    
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'), 
    path('browse_routes/', views.browse_routes, name='browse_routes'),
    
    
    path('user_dashboard/', views.user_dashboard, name='user-dashboard'),   
    path('operator_dashboard/', views.operator_dashboard, name='operator-dashboard'),   
]