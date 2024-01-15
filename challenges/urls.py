from django.urls import path
from . import views

urlpatterns = [
    path("",views.index , name = "index"),  #/challenges
    path("<int:month>",views.months_challenges_by_number),
    path("<str:month>",views.months_challenges , name = "month-challenge")
    
]