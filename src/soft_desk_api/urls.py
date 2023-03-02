"""soft_desk_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from auth.views import UserViewset, RegisterView
from ITS.views import (ProjectListViewset, ProjectDetailViewset, IssuesViewset, 
                       ContributorsViewset, DeleteContributorViewSet, CommentsViewset)

router = routers.SimpleRouter()
#router.register('project', ProjectListViewset.as_view(), basename='project')
#router.register('issues', IssuesViewset, basename='issue')
#router.register('contributors', ContributorsViewset, basename='contributor')
#router.register('comments', CommentsViewset, basename='comment')
router.register('user', UserViewset, basename='user')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/signup/', RegisterView, name='register'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/', include(router.urls)),
    path('api/project/', ProjectListViewset.as_view(), name='project-list'),
    path('api/project/<int:pk>/', ProjectDetailViewset.as_view(), name='project-detail'),
    path('api/project/<int:project_id>/users/', ContributorsViewset.as_view(), name='contributors-list'),
    path('api/project/<int:pk>/users/<int:user_id>/', DeleteContributorViewSet.as_view(), name='contributors-delete'),
    path('api/project/<int:project_id>/issues/', IssuesViewset.as_view(), name='issue-list'),
    #path('api/project/<int:pk>/issues/<int:issue_id>/comment/', CommentsViewset, name='comment-list'),
]
