"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

'''
전체 url은 urls.py를 진입하면서 parsing 됨 !
include() -> URLconf 모듈을 통합하도록 설계 
path() 함수는 특정경로에 대해 include('polls.urls')를 호출 
ex. 유저가 /polls/detail/5/로 접근시 -> 
                                    1. mysite/urls.py에서 path('polls/', include("polls.urls"))를 통해 일치경로 'polls'를 파악 후 제거
                                    2. 제거된 url /detail/5가 polls/urls.py로 이동하여 순차적으로 처리 
'''

urlpatterns = [
    path('polls/', include("polls.urls")), # 최상위(mysite)의 URLconf와 앱(polls)의 URLconf 연결 즉,
    path('admin/', admin.site.urls),
]
