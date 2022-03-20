from django.urls import path
from games.seek.views import seek

urlpatterns = [  
    path('', seek),  # app homepage
]  
