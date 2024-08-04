from django.contrib import admin
from django.urls import path, include
#changed views name in case there's multiple views
from todolist_app import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_views.index, name= 'index'),
    # Always remember urls(route), views(function/render/response), template(html)
    path('todolist/', include('todolist_app.urls')),
    path('account/', include('users_app.urls')),
    path('contact', todolist_views.contact, name='contact'),
    path('about', todolist_views.about, name='about'),
]
