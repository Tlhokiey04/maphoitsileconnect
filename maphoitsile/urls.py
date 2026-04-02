from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/',                    admin.site.urls),
    path('',                          views.user_login,   name='login'),
    path('register/',                 views.register,     name='register'),
    path('logout/',                   views.user_logout,  name='logout'),
    path('accounts/dashboard/',       views.dashboard,    name='dashboard'),
    path('reports/',                  views.issue_list,   name='issue_list'),
    path('reports/new/',              views.report_issue, name='report_issue'),
    path('reports/<int:pk>/',         views.issue_detail, name='issue_detail'),
    path('reports/<int:pk>/success/', views.issue_success,name='issue_success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)