from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.movie_form,name='movie_insert'),
    path('<int:id>/', views.movie_form, name='movie_update'),
    path('list/', views.movie_list,name='movie_list'),
    path('delete/<int:id>/', views.movie_delete,name='movie_delete')

]