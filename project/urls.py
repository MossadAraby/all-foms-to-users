from django.contrib import admin
from django.urls import path,include
from django.conf import settings as st
from django.conf.urls.static import static as sc
from django.contrib.auth import views as auth_views
from testapp import views



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('login/', views.login, name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('social-auth/', include('social_django.urls', namespace='social')),
#     path("", views.home, name='home'),
# ]



urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('testapp.urls',namespace='test')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]

if st.DEBUG:
    urlpatterns += sc(st.STATIC_URL,document_root=st.STATIC_ROOT)
    urlpatterns += sc(st.MEDIA_URL,document_root=st.MEDIA_ROOT)