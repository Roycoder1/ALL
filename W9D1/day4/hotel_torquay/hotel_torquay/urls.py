"""hotel_torquay URL Configuration

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
from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("torquay.urls")),
    path('login/', LoginView.as_view()),
    path("signout", LogoutView.as_view(template_name = '/Users/benisti/Desktop/DI_Bootcamp_Stage1/W9D1/day4/hotel_torquay/account/templates/signout.html')),
    path("accounts/",include("account.urls")),
]
