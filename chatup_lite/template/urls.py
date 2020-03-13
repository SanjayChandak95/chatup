"""groceryList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from groceryList_lite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.home_view,name = "Home_View"),
    path('signUp/',views.signUp_view,name = "SignUp_View"),
    path('login/',views.login_view,name = "Login_View"),
    path('createTitle/',views.title_view,name = "Title_View"),
    path('logout/',views.logout_view,name ="Logout_view"),
    path('groceryTitle/<int:id>',views.groceryContent_view,name='GroceryContent_View'),

    #path('deleteGroceryTitleForm',views.deleteTitles_view,name='GroceryContent_View'),
    path('deleteGroceryTitle/<int:id>',views.deleteTitle_view,name='DeleteGroceryTitle_View'),
    path('deleteGroceryContent/<int:id>',views.deleteContent_view,name='DeleteGroceryContent_View'),
    path('deletesharedUser/<int:id>',views.deleteSharedUser_view,name='deleteSharedUser_View'),
    path('newSharedUser/<int:id>',views.newSharedUser_view,name='newSharedUser_View')
]
