from django.urls import path
from .views import *

urlpatterns = [
    
    # api/accounts/
    path("send-data/", IncomingDataView.as_view(), name="test-url"),
    path("save-account/", SaveAccount.as_view(), name="save-account"),
    path('destinations/<str:account_id>/', GetDestinations.as_view(), name="destinations"),
    path("destination/save-destination/", CreateDestination.as_view(), name="save-destination"),
    path('delete-account/<str:account_id>/', DeleteAccount.as_view(), name="delete-account"),
    path('edit-destination/<int:destination_id>/', EditDestination.as_view(), name="edit-destination"),
    path('delete-destination/<int:destination_id>/', DeleteDestination.as_view(), name="delete-destination"),
    path('show-account/<str:account_id>/',ShowAccount.as_view(),name="show-account"), 
    path('edit-account/<str:account_id>/',EditAccount.as_view(),name="edit-account")
]
