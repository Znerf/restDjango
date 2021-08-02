
from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt   

# fro/m
from rest_framework.routers  import DefaultRouter


router=DefaultRouter()
router.register('user',views.UserViewSet, basename='user')
urlpatterns = [
    # path('', views.home , name='home'),
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>',include(router.urls)),


    path('user/',views.userList.as_view()),
    path('userAPI/',views.UserAPIView.as_view()),
    path('userAPI/<int:id>/',views.UserDetail.as_view()),
    
    path('userGen/',views.GenericAPIView.as_view()),

    path('userGen/<int:id>/',views.GenericAPIView.as_view()),

    path('userFun/',csrf_exempt(views.user_list)),
    path('userFun/<int:pk>/',csrf_exempt(views.user_detail))


    
]