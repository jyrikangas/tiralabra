Ohjelman rakenne:

app.py alustaa pelilaudan (8x8 matriisi), ja aloittaa sovelluksen pääsilmukan. Silmukassa on sovelluksen pygamea käyttävä käyttöliittymä, jonka kautta käyttäjä voi siirtää pelinappuloita. 

Silmukasta kutsutaan gamelogic.py ja AiPlayer.py tiedostoja. gamelogic.py sisältää metodit joilla sovellus selvittää nappuloille mahdolliset siirrot. legal() metodi antaa parametrina annetulle nappulalle kaikki lailliset siirrot jotka ovat mahdollisia parametrina annetulla pelilaudalla. promotion() mahdollistaa sotilasnappulan ylennyksen, jossa ylennys valitaan tekstikäyttöliittymän kautta.

AiPlayer.py sisältää tekoälyyn liittyvät metodit. choosemove2() kokeilee kaikkia tekoälylle mahdollisia siirtoja, ja palauttaa niistä parhaan. choosemove2() kutsuu metodia alphabeta() joka palauttaa arvion siirron arvosta. alphabeta() on alphabeta-karsinnalla tehostettu minimax-algoritmi. Se kutsuu metodia boardValue() joka laskee yhteen kaikki pelilaudalla olevat nappulat ja palauttaa numerollisen arvion siitä paljonko tekoälypelaaja on voitolla tai häviöllä.

AiPlayer.py tiedoston doMove() metodi toteuttaa sille parametrina annetun siirron, ja palauttaa pelilaudan, jossa siirto on toteutettu.

piece.py ja move.py ovat olioita jotka kuvaavat pelinappuloita ja siirtoja. Piece -olioilla on puoli ("b" tai "w"), hahmo (kuningas "K", ratsu "N", kuningatar "Q" jne.), sijainti pelilaudalla (koordinaatit) ja lista, joka sisältää siirrot jotka nappula voi tehdä. Lisäksi oliolla on metodi sijainnin päivittämiseen setPos(), ja olio pitää kirjalla onko se liikkuunut kertaakaan (bool hasMoved), ja onko nappula pelissä (bool alive).

Move-oliolla on siirron aloitusruutu (origin), päämääräruutu (square) ja viite päämääräruudussa mahdollisesti olevaan nappulaan (squarecontent). Lisäksi Move-olio voi olla ylennys, ja oliolle voidaan asettaa arvo.

Suorituskyky:

Minmax+alphabeta-algoritmi pystyy käymään läpi 3 siirron syvyyden n.minuutin+ ajassa.

Puutteet ja parannettava:

Kaikki shakin säännöt eivät toteudu, esim en passant. Lisäksi tekoälyssä on optimoinnin varaa, ja käyttöliittymä on huono.


Lähteitä:

https://en.wikipedia.org/wiki/Alpha-beta_pruning
https://en.wikipedia.org/wiki/Minimax
https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/

