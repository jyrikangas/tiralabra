Testaus:

gametest.py tiedostossa sijaitsevissa testeissa testataan mm. tekoälyn kykyä huomata ja välttää häviö, valita voittava siirto, sekä muutamia yksittäisiin toimintoihin kuten linnoitukseen ja ylennykseen liittyviä testejä.

Testeissä yleensä alustetaan pelitilanne ja kutsutaan testattavaa metodia: esim testissä test_win_in_depth_3 alustetaan tilanne jossa tekoälyn on mahdollista poistaa vastustajan sotilas pelistä heti, tai ohittaa sotilas jotta ensi vuorolla voi voittaa pelin. Tämän testin suoritus osoittaa että tekoäly pystyy huomaamaan voiton minmax syvyydellä 3.

