from django.urls import path
from .views import login, home, predict, user, game, hackathon, play, solar_energy, energy_consumption, solar_radiation

urlpatterns = [  
    path('', login , name= "login"),
    path('colar/', home , name= "home"),
    path('colar/predict/' , predict , name= "predict"),
    path('colar/hackathon/', hackathon , name= "hackathon"),
    path('colar/hackathon/solar_energy',solar_energy , name= "solar_energy"),
    path('colar/hackathon/solar_radiation', solar_radiation , name= "solar_radiation"),
    path('colar/hackathon/energy_consumption', energy_consumption , name= "energy_consumption"),
    path('colar/game/', game , name= "game"),
    path('colar/game/play', play , name= "play"),
    path('colar/user/', user , name= "user"),
]