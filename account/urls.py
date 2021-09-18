from django.urls import path
from account.views import (
    registration_view, user_delete_view,
    approvedUser_detail_view, approve_pending_user_view, ChangePasswordView,
    nonapprovedUser_detail_view, CustomAuthToken, UpdateUserView, RetrieveUserView,isAdminView, ListCreateRolesView
)

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
    path('register/', registration_view, name="register"),
    path('approve_user', approve_pending_user_view, name="approve_user"),
    path('roles/', ListCreateRolesView.as_view(), name='create_role'),
    path('show_approvedUsers', approvedUser_detail_view, name="show_all_approved_users"),
    path('show_nonapprovedUsers', nonapprovedUser_detail_view, name="show_all_nonapproved_users"),
    path('login/', CustomAuthToken.as_view(), name="login"),
    path('<slug>/delete_user', user_delete_view, name="delete_user"),
    path('change_password/<str:email>/', ChangePasswordView.as_view(), name='change password'),
    path('update/<str:email>/', UpdateUserView.as_view(), name='update user'),
    path('<int:pk>/', RetrieveUserView.as_view(), name='retrieve user'),
    path('isadmin/', isAdminView, name='Check if user id admin'),

]
