from views import ProcessMailAPIView
from django.urls import path



urlpatters =[
   path( "/process-email", ProcessMailAPIView.as_view())
]