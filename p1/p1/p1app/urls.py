
from django.urls import path

from p1app import views
app_name='p1app'

urlpatterns = [
    path('',views.demo,name='demo'),
    path('movie/<int:movie_id>/', views.detail,name='detail'),
    path('add/', views.data, name='data'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete')

]