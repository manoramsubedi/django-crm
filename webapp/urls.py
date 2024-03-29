from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),

    #CRUD
    path('dashboard', views.dashboard, name="dashboard"),

    path('add-record', views.add_record, name="add-record"),

    path('update/<int:pk>', views.update, name="update"),

    path('view/<int:pk>', views.single_record, name="view"),

    path('delete-record/<int:pk>', views.delete, name="delete"),

]