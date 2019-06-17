from django.urls import path
from .views import home,detailPost,book, signuppage, signout, Addplace, loginpage

app_name='myapp'
urlpatterns = [
    path('', home,name='home'),
    path('post/<slug:id>/', detailPost, name='detailPost'),
    path('book/', book, name='book'),
    path('login/',loginpage,name='login'),
    path('signup/',signuppage,name='signup'),
    path('logout/',signout,name='logout'),
    path('addplace/',Addplace.as_view(),name='addplace'),


]