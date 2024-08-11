from django.urls import path
from .views import CountryListCreate, CountryDetail

urlpatterns = [
    path('countries/', CountryListCreate.as_view(), name='country-list-create'),
    path('countries/<int:pk>/', CountryDetail.as_view(), name='country-detail'),
]

