from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('eduprod/', include('eduprod.urls')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('eduprod/', include(('eduprod.urls', 'eduprod'), namespace='eduprod')),
    path('accounts/login/', include('users.urls')),
=======
    path('eduprod/', include(('eduprod.urls', 'eduprod'), namespace='eduprod')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('accounts/login/', include('users.urls')),
]
>>>>>>> cfc08ec00746f3da863f0a48433843eb0dc53ce0
