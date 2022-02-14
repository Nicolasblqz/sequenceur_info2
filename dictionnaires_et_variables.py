# dicos pour l'instant mais à changer en classes ?

PARAM1 = {"note":0, "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0}
PARAM2 = {"note":0, "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0}
# ...
SEQ = {"pas1":PARAM1, "pas2":PARAM2}

GEN = {"long":0, "bpm":0, "gamme":0}


# pins et autres (adapter avec le produit de philippe)

# Définit les pins utilisé par les encodeurs (n° encodeur,clk,dt,sw). Si on utilise pas le sw, notez False
encoder_1 = (1,13,19,26)
encoder_2 = (2,5,6,False)
encoder_3 = (3,10,11,False)
encoder_4 = (4,20,21,False)
encoder_5 = (5,12,16,False)
encoder_6 = (6,8,7,False)
encoder_7 = (7,24,25,False)
encoder = [encoder_1,encoder_2,encoder_3,encoder_4,encoder_5,encoder_6,encoder_7]

# Définit les valeurs initiales des encodeurs
val = [0,0,0,0,0,0,0]

# Définit les paliers en fonction des encodeurs
step = [int(4096/(12*5)),1,1,1,1,1,1]

# pDéfinit l'intervalle des encodeurs
interval = [(0,4096),(-20,20),(-20,20),(-20,20),(-20,20),(-20,20),(-20,20)]


# écran
# pas les bonnes versions sur github
