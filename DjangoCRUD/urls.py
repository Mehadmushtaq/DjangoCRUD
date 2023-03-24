from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CRUD.urls')),
    path('add', include('CRUD.urls')),
    path('edit', include('CRUD.urls')),
    path('update/<str:id>', include('CRUD.urls')),               #way to pass id
    path('delete/<str:id>', include('CRUD.urls')),
]
