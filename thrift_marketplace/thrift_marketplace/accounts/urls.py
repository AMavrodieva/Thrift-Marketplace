from django.urls import path, include
from thrift_marketplace.accounts.views import AppSignInUserView, AppSignUpUserView, AppSignOutUserView, \
    AppEditUserView, AppDetailsUserView, HomePageView, delete_user

urlpatterns = (
    path('login/', AppSignInUserView.as_view(), name='login user'),
    path('register/', AppSignUpUserView.as_view(), name='register user'),
    path('logout/', AppSignOutUserView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', HomePageView.as_view(), name='home page'),
        path('details/', AppDetailsUserView.as_view(), name='details user'),
        path('edit/', AppEditUserView.as_view(), name='edit user'),
        path('delete/', delete_user, name='delete user'),
    ])),
)