#Hier maak ik een klok in Python
seconden = 45
minuten = 59
uren = 23

import time
#hier wordt de tijd op het scherm weergeven met de print
while True:
     print(str(uren).zfill(2) + ":" + str(minuten).zfill(2) + ":" + str(seconden))
     seconden = seconden + 1
     time.sleep(1)
     #hier weet de computer wat het moet doen als de timer 60 seconden raakt, en dat is er een minuut bij rekenen
     if seconden == 60:
         seconden = 0
         minuten = minuten + 1
     #hier weet de computer wat het moet doen als de timer 60 minuten raakt, en dat is er een uur bij rekenen
     if minuten == 60:
        minuten = 0
        uren = uren + 1
     #hier weet de computer wat het moet doen als de timer 24 uur raakt, en dat alles weer op 0 zetten en opnieuw tellen
     if uren == 24:
          uren = 0 
          minuten = 0
          seconden = 0
        
      
