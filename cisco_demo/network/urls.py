from django.urls import path
from network.views import *
app_name = 'network'

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('api/routers', RouterListView.as_view(), name='PersonListView'),
    path('api/router/<int:pk>', RouterDetailView.as_view(), name='ProductDetailView'),
]