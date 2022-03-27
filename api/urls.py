from django.urls import path
from .views import AirdropView, BurnView, SingleBalance, SingleLog, PeerView

urlpatterns = [
    path('airdrop/', AirdropView.as_view(), name='airdrop'),
    path('burn/', BurnView.as_view(), name='burn'),
    path('peer/', PeerView.as_view(), name='peer'),

    path('balance/<int:pk>', SingleBalance.as_view(), name='balance'),
    path('log/<int:pk>', SingleLog.as_view(), name='log'),

]
