from django.urls import path
from .views import *

urlpatterns = [

    path('', SnackListView.as_view(), name = 'snack_list'),
    path('<int:pk>/', SnackDetailView.as_view(),name = 'snack_detail'),
    path('<int:pk>/delete/',SnackDeleteView.as_view(), name = 'snack_delete'),
    path('create/',SnackCreateView.as_view(), name = 'snack_create'),
    path('<int:pk>/update/', SnackUpdateView.as_view(), name = 'snack_update')
]