"""
URL configuration for wallet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.urls import path
from .views import WalletBalanceView, WalletTopUpView, WalletBonusView, WalletSpendView

urlpatterns = [
    path('wallet/<int:user_id>/<int:asset_type_id>/balance/', WalletBalanceView.as_view()),
    path('wallet/<int:user_id>/<int:asset_type_id>/topup/', WalletTopUpView.as_view()),
    path('wallet/<int:user_id>/<int:asset_type_id>/bonus/', WalletBonusView.as_view()),
    path('wallet/<int:user_id>/<int:asset_type_id>/spend/', WalletSpendView.as_view()),
]
