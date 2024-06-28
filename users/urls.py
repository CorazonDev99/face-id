from django.urls import path
from .views import *

urlpatterns = [
    path('auth/', UploadPhoto.as_view(), name='user-auth'),
    path('recognize/', RecognizePhoto.as_view(), name='recognize'),
]
