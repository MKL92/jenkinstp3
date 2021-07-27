import time
 
# Obtenir l'heure et la date locale
now = time.localtime(time.time())
 
print time.asctime(now) # Afficher la date en format lisible
 
# Personnaliser les formats d'affichage des dates
print time.strftime("%y/%m/%d %H:%M", now)
print time.strftime("%a %b %d", now)
print time.strftime("%c", now)
print time.strftime("%I %p", now)
print time.strftime("%Y-%m-%d %H:%M:%S %Z", now)
 
year, month, day, hour, minute, second, weekday, yearday, daylight = now
print "%04d-%02d-%02d" % (year, month, day)
print "%02d:%02d:%02d" % (hour, minute, second)
print ("Lun", "Mar", "Mer", "Jeu", "Ven", "SAM", "Dim")[weekday], yearday
 
"""
Sat Aug 25 13:06:31 2012
12/08/25 13:06
sam. août 25
sam. août 25 13:06:31 2012
01 PM
2012-08-25 13:06:31 CEST
2012-08-25
13:06:31
SAM 238
"""
