# Πρόγραμμα "παραλήπτης"
# 1. Λαμβάνει δεδομένα από το πρόγραμμα "αναμεταδότη"
# 2. Υπολογίζει το υψόμετρο από την τρέχουσα ατμοσφαιρική πίεση
# 3. Στέλνει όλα τα δεδομένα στη θύρα USB

from microbit import *
import math
import make_radio

# Ατμοσφαιρική πίεση στο επίπεδο της θάλασσας σε (Pa)
p0=101325

radio = make_radio.MakeRadio(group=5)
radio.off()
radio.on()

while True:
    message=radio.receive_packet()
    if message:
        k=message[:4]
        if k=="Pres":
            Ps = int(str(message[5:]))
            Alti = 44330 * (1 - math.pow((Ps/p0),(1/5.255)) )
            print('Pres:%.2f' %Ps)               
            print('Alti:%.2f' %Alti)
        else:
            print(message)
