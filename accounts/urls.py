from django.urls import path
from .views import *
urlpatterns = [
    
    path("incoming-data/", IncomingDataView.as_view(), name="test-url"),
    path("save-account/", SaveAccount.as_view(), name="save-account"),
    path('destinations/<str:account_id>/', GetDestinations.as_view(), name="destinations"),
    path("destination/save-destination/", CreateDestination.as_view(), name="save-destination"),
    path('delete-account/<str:account_id>/', DeleteAccount.as_view(), name="delete-account")

]