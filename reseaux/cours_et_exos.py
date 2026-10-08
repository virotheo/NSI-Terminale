'''
IP = 192.168.12.4/24 Masque = 255.255.255.0
Partie réseau = 192.168.12 Partie Mmachine = 4
255 = 11111111
0 = 00000000
1 = réseau 0 = machine


Exercice 1 

1) LIP commence par 179.19.1.X, le masque pour 39 machines sera donc 255.255.255.X et X
 correspond à 255-39 soit 216 donc 255.255.255.216
 correction : 
  39 machines + 2 soit 41 places
  11 000000 on bloque les 6 derniers bits soit 2⁶ = 64 possibilités 
  11 = 64 + 128 = 192 donc le masque sera de 255.255.255.192
   
2) L'IP commence par 192.168.X.X, le masque pour 500 machines donc besoin de 502 la plus petite
 puissance de 2 est entre 256 et 512, 2⁹ = 512 donc 9 zeros donc :
 11111111.11111111.11111110.00000000
 255.255.254.0
 broadcast = 255.255.255.255

Exercice 2

1) A = 192.168.0.1/16  B = 192.168.10.1/16
 la partie réseau est sur les 2 premiers octets 192.168 pour le A et 192.168 pour le B donc les
 parties réseaux sont identiques donc les 2 ordianteurs peuvent communiquer entre eux.
2) A = 192.168.0.1/24  B = 192.168.10.1/24
 la partie réseau est sur les 3 premiers octets 192.168.0 pour le A et 192.168.10 pour le B
 donc les parties réseaux sont différentes donc les deux ordinateurs ne peuvent pas communiquer entre
 eux.
3) A = 192.168.240.1/20  B = 192.168.251.12/20
la partie réseau se lie sur les 20 premiers octets donc les 2 premiers vont jusqu'a 16 et il 
 manque les 4 bits suivants soit 128+64+32+16 = 240 donc les deux ordinateurs peuvent communiquer
 entre eux
4) A = 192.168.240.1/20  B = 192.168.238.12/20
 la partie réseau se lie sur les 20 prmeiers bits soit sur les deux premiers octets plus les 4 
 bits suivants donc A = 11000000.10101000.11110000.00000000 donc partie reseau du A  = 11000000.10101000.1111
 et B = 11000000.10101000.11101110.(12 en binaire) donc la partie reseau est B = 11000000.10101000.1110 donc 
 le dernier bit du reseau est différent avec le A donc les deux ordinateurs ne peuvent pas communiquer ente
  eux.


NB = 192.168.0.1/24 est appellée la notation CIDR
Exercice 3 (Filius)


'''
