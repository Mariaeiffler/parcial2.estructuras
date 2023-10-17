import pickle
try:
    with open('hotel.pickle', "rb") as f: 
        objeto_cargado = pickle.load(f)
except: #crear objeto hotel