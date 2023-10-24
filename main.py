import pickle
from hotel import Hotel 
try:
    with open('hotel.pickle', "rb") as f: 
        hotel = pickle.load(f)
        
except: #crear objeto hotel
    hotel=Hotel('Patagonia: Oasis y Ocio')
    hotel.entrar()
    hotel.save()

print(hotel.empleados)
