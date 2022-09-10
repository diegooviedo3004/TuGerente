from django.urls import path
# Im aware that i can import all of them in a single line
# But I thinks this ways more explicit
from .views import ReservationList, ReservationDetail
from .views import PaymentMethodList, PaymentMethodDetail
from .views import StatusList, StatusDetail
from .views import ClientDetail, ClientList

urlpatterns = [
    # Handles the Reservation endpoints
    path('reservation/', ReservationList.as_view()),
    path('reservation/<int:pk>/', ReservationDetail.as_view()),

    # Handles the Payment Method endpoints
    path('payment/', PaymentMethodList.as_view()),
    path('payment/<int:pk>/', PaymentMethodDetail.as_view()),

    # Handles the Status endpoints
    path('status/', StatusList.as_view()),
    path('status/<int:pk>/', StatusDetail.as_view()),

    # Handles the Client endpoints
    path('client/', ClientList.as_view()),
    path('client/<int:pk>/', ClientDetail.as_view()),

]