from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('roles/', RolesCreateView.as_view(), name='role_create'),
    path('roles/<int:pk>', RolesRetrieveView.as_view(), name='role_retrieve'),

    path('registration/', RegistrationAPIView.as_view(), name='registration'),

    path('login/', LoginAPIView.as_view(), name='login'),

    path('user/', UserRetrieveUpdateAPIView.as_view(), name='user'),

    # path('getusertoken', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('getusertokenrefresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
