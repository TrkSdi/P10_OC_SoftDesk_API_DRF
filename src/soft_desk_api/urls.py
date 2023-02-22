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

from ITS.views import (ProjectViewset, IssuesViewset, 
                       ContributorsViewset, CommentsViewset,
                       AdminProjectViewset, AdminContribViewset,
                       AdminIssuesViewset, AdminCommentsViewset)

router = routers.SimpleRouter()
router.register('project', ProjectViewset, basename='project')
router.register('issues', IssuesViewset, basename='issues')
router.register('contributors', ContributorsViewset, basename='contributors')
router.register('comments', CommentsViewset, basename='comments')
router.register('admin/project', AdminProjectViewset, basename ='admin-project')
router.register('admin/contributors', AdminContribViewset, basename ='admin-contrib')
router.register('admin/issues', AdminIssuesViewset, basename ='admin-issues')
router.register('admin/comments', AdminCommentsViewset, basename ='admin-comments')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls))
]
