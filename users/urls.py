from django.urls import path
from users.views import *

app_name = 'food'

urlpatterns = [
    path('roles/', RolesCreateView.as_view(), name='role_create'),
    path('roles/<int:pk>', RolesRetrieveView.as_view(), name='role_retrieve'),

    path('user/', UserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/', UserRetrieveView.as_view(), name='user_retrieve'),

    # path('getusertoken', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('getusertokenrefresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
