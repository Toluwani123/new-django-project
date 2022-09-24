from django.urls import path
from .views import BankDelete, BankList, BankDetails, BankCreate, BankUpdate, AccountLogin, RegisterUser, qr_code
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', AccountLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('', BankList.as_view(), name="banks"),
    path('bank/<int:pk>/', BankDetails.as_view(), name="bank"),
    path('create-bank/', BankCreate.as_view(), name='bank-create'),
    path('bank-update/<int:pk>/', BankUpdate.as_view(), name='bank-update'),
    path('bank-delete/<int:pk>', BankDelete.as_view(), name='bank-delete'),
    path('qr-code',qr_code,name='qr_code' )
]