# ViikkoRaportit
Dokumentissa on projektin viikkoraportit, jotka sisältää:
- Mitä olen tehnyt viikolla?
- Miten projekti on edistynyt?
- Mitä opin viikolla?
- Mikä jäi epäselväksi tai tuottanut vaikeuksia?
- Mitä teen seuraavaksi?
- Kuinka paljon käytin aikaa projektiin viikolla?



## Viikkoraportti 1
### Mitä olen tehnyt viikolla?
Valitsin aiheeksi signaalinprosessoinnin ja kohinanpoiston. Ohjaajan kanssa tarkensimme projektin aiheen FFT(Fast Fourier Tranform) algoritmin käyttämiseen ja soveltamiseen.
Tämän pohjalta alustin projektin repositorion ja dokumentaation.
### Miten projekti on edistynyt?
Projektin repositorio on alustettu.
### Mitä opin viikolla?
Signaalinprosessoinnista on suhteellisen hankala löytää materiaalia, josta oppia.
Suuri osa materiaalista kohdistuu valmiisiin kirjastoihin, jotka tekevät työn jo valmiiksi.
### Mikä jäi epäselväksi tai tuottanut vaikeuksia?
Äänitiedoston manipulointi FFT:lle sopivaan muotoon. En tiedä aivan mistä aloittaa. Mitä tietoa saan äänitiedostosta irti ja miten?

### Mitä teen seuraavaksi?
Toteutan Tkinter kirjastolla yksinkertaisen graafisen käyttöliittymän ja tutustun FFT:hen enemmän. Toteutan FFT algoritmin. 
### Kuinka paljon käytin aikaa projektiin viikolla?
Käytin noin 3h aikaa tällä viikolla projektiin



## Viikkoraportti 2
### Mitä olen tehnyt viikolla?
Rakensin yksinkertaisen käyttöliittymän käyttäen Tkinter:iä.

Tutustuin FFT algoritmiin erinäisin videoin ja artikkelein.

Luin Cooley-Tukey algoritmiin tarkemmin Wikipedia-artikkelin pohjalta.
### Miten projekti on edistynyt?
Yksinkertainen käyttöliittymä luotu
### Mitä opin viikolla?
FFT Toiminnasta:
FFT Toimii pienellä määrällä dataa verrattuna FT, joka vaatii jatkuvan signaalin. FFT löytää signaalista sini-aallot tutkimalla jaksottain signaalia. Toistuvaan aaltoon osuessaan fft antaa merkittävästi korkeamman arvon.

FFT käyttötilanteista:
- Äänen jakaminen perusosiin
- Kuvien kompressointi
- Ydinpommien räjähdysten tunnistaminen seismografin tulosteesta
- laadun hallita laitteistot

Tkinter:n käyttämisestä laajemmin [ohjetta](https://tkdocs.com/tutorial/index.html) seuraten.
### Mikä jäi epäselväksi tai tuottanut vaikeuksia?
Tällä hetkellä on epäselvää se, miten tulen lukemaan äänitiedostot FFT:lle. En ole vielä tutustunut miltä .wav tiedostot näyttävät bittitasolla/miten saan niistä haluamani tiedon ulos.

Vaikuttaisi siltä, että scipy kirjastolla pystyy lukemaan wav tiedostoja. En kuitenkaan ole varma olisiko tämä sellainen asia, joka tulisi toteuttaa itse.
### Mitä teen seuraavaksi?
- Tutustun .wav tiedostojen lukemiseen
- Toteutan Cooley-Tukeyn algoritmin
- Tutustun lisää FFT algoritmin käyttöön
### Kuinka paljon käytin aikaa projektiin viikolla?
8h



## Viikkoraportti 3
### Mitä olen tehnyt viikolla?
Tutustunut lisää [FFT:n toteuttamiseen](https://www.csd.uwo.ca/~mmorenom/CS433-CS9624/Resources/Implementing_FFTs_in_Practice.pdf).


### Miten projekti on edistynyt?
fft.py moduuli luotu, jossa fft algoritmi toteutettu.

moduuli on tällä hetkellä kirjoitettu pelkästään oppimista ja testausta varten.

### Mitä opin viikolla?
FFT on hyvin hankala käsittää, koska se hyödyntää kompleksilukuja ja yksikköjuuria. Youtube kanavan 3Blue1Brown [video](https://www.youtube.com/watch?v=spUNpyF58BY) aiheesta antoi intuitiivisen ymmärryksen algoritmin tuloksesta, mutta ei auta yhtään (ainakaan itseäni) algoritmin ymmärtämisessä. [Artikkeleiden](https://www.csd.uwo.ca/~mmorenom/CS433-CS9624/Resources/Implementing_FFTs_in_Practice.pdf) lukeminenkaan ei ole auttanut, koska tuntuu, että ne ovat taas hieman liian korkealla tasolla. Pseudokoodia ja yhtälöiden muuttujia ei avata ihan tarpeeksi.

Tähän mennessä paras lähde algoritmin toiminnan sisäistämiselle on ollut Youtube kanavan Reducible [video](https://www.youtube.com/watch?v=h7apO7q16V0), jossa hän purkaa algoritmin matematiikan yksinkertaisista tuloksista alkaen. Lisäksi hänen [jatko-osa](https://www.youtube.com/watch?v=h7apO7q16V0) aiheesta auttoi myös jonkun verran.

Opin tarkemmin mitä FFT tekee prosessoidessaan:
Toteuttamani algoritmi on syvyys ensin tyyppinen. Se jakaa datan puoliksi parillisiin ja parittomiin rekursiolla kunnes datan pituus on 1. Sillon se palauttaa data.  Palautettu data vastaanotetaan parilliseen ja parittomaan muuttujaan, eli kummassakin on yksi arvo tässä vaiheessa.

Seuraavaksi suoritetaan ensimmäinen muunnos käyttämällä yksikköjuuria. Yksikköjuuret ovat kompleksilukuja, jotka kertovat kaikki pituuden 1 vektorit, jotka korotettuna potenssiin n antaa arvoksi 1. Algoritmissa otetaan aina datan pituuden verran yksikköjuuria eli tässä tilanteessa 2. Yksikköjuuret lasketaan Eulerin kaavan avulla. Seuraavaksi suoritetaan muunnos datalle, jota en aivan ymmärrä vielä. Tämä muunnos on se FFT:n taika. Muunnoksen tulos palautetaan parillisen tai parittoman muuttujaan ja kierros alkaa alusta. Tämä jatkuu kunnes data on käyty läpi.

### Mikä jäi epäselväksi tai tuottanut vaikeuksia?
Mitä FFT:n muunnos tarkalleen tekee/ miten se toimii.

### Mitä teen seuraavaksi?
Muokkaan käyttöliittymää niin, että siinä on oma sivu kuvaajien piirtämiselle/ data analysoinnille.

Implementoin FFT algoritmin käyttöliittymään:
- Kirjoitan FFT:n kutsuttavaan muotoon.
- Otan FFT:n käyttöliittymässä käyttöön.

Tutkin FFT:n käyttöä datan muokkaamisessa.

### Kuinka paljon käytin aikaa projektiin viikolla?
14h



## Viikkoraportti 4
### Mitä olen tehnyt viikolla?
refaktoroinut fft.py kutsuttavaan muotoon.

Lisännyt kayttoliittyma.py moduuliin valikko, josta pääsee navigoimaan tuleviin välilehtiin.

Tutkinut fft:n avulla äänen filtteröintiä.

Sain testatessa tuotettua ensimmäisen wav tiedoston prosessoidusta datasta. Se kuulosti hieman hassulle, koska käytin kaksi kanavaista lähdettä, josta prosessoin vain toisen.

### Miten projekti on edistynyt?
- fft.py refaktoroitu kutsuttavaan muotoon versio 1.
- kayttoliittymä.py lisätty valikko

### Mitä opin viikolla?
fft:n käänteisalgoritmi ifft:n totettaminen on hyvin helppoa, jos fft on toteutettu, koska aino, joka muuttuu algoritmissa on yksikköjuuret. Yksikköjuuret muuttuvat muotoon 1/yksikköjuuri.

Tkinter ikkunoidenhallintaa. Yrittäessäni luoda käyttöliittymään valikkoa tuli ongelma, jossa valikko avautui uuteen ikkunaan. On tärkeää, että kutsuu samaa Tk objektia tai muuten syntyy lisää ikkunoita.

### Mikä jäi epäselväksi tai tuottanut vaikeuksia?
Tällä hetkellä fft.py prosessoi vain ensimmäisen äänikanavan tiedostoista. Aloin toteuttamaan usean kanavan prosessointia, mutta se meni monimutkaiseksi ja päätin jättää sen myöhemmäksi. Sain jaettua äänikanavat, mutta en ihan ymmärtänyt vielä miten ne tulisi liittää takaisin yhteen wav tiedostoon.

### Mitä teen seuraavaksi?
- Toteutan käyttöliittymän välilehdet ja yhdistän ne valikkoon.
- Yhdistän visualisointi välilehdelle fft.py kuvaajien piirtämistä
- Toteutan äänenfiltteröinnin taajuuden mukaan.

- Laaja Dokumentaation läpikäynti ja uusinta

- Testauksen kirjottaminen fft.py

### Kuinka paljon käytin aikaa projektiin viikolla?
20h hidasta työaikaa



## Viikkoraportti 5
### Mitä olen tehnyt viikolla?
- Luotu uusia testi-tiedostoja, joita on helpompi tulkita fft muodossa.
- Valikko toimii nyt. (Kaikkia valikon ruutuja ei ole vielä lisätty.)
- Vaihdoin fft.py nimen aanenprosessointi.py, koska halusin, että nimi kuvaisi paremmin tulevaa moduulin toimintaa.
- Vahvimman signaalin havaitseminen ja poistaminen on nyt implementoitu.
- aanenprosessointi.py yksittäin suorittaessa saa luotua prosessoidun äänitiedoston, josta voi havaita signaalinpoiston.

### Miten projekti on edistynyt?
- kayttoliittyma.py valikko toimii nyt ja voi siirtyä ruudulta toiselle.
- Vahvimman signaalin havaitsemis- ja poistamisfunktio on luotu.

### Mitä opin viikolla?
Projektin edetessä tuntuu, että kehitys hidastuu, kun integraation taso kasvaa. Olin varma, että saisin tällä viikolla jo implementoitua äänenprosessoinnin käyttöliittymään, mutta se ei tapahtunut.

Projektin jakaminen ajatuksella moduuleihin, luokkiin ja funktioihin auttaa todella paljon projektin jatkokehityksessä. kayttoliittyma.py jakaminen luokkiin teki siitä paljon selvemmän ja miellyttävämmän näköisen ja jatkossa siihen on paljon helpompi palata.

Tkinter koodi tuntuu paisuvan nopeasti aika monimutkaiseksi, joten sen organisointi oli erityisen tärkeää.

Opin Tk toplevel ikkunoista, kun käyttämäni [tk-ohje](https://tkdocs.com/tutorial/index.html) käytti sitä selittämättä sitä kunnolla. Omassa koodissa toplevel() komento aiheutti ongelmia ja loi ylimääräisen ikkunan. Lopulta selvisikin, että toplevel() luo uuden toplevel ikkunan, jota omassa tilanteessani en halunnut.



### Mikä jäi epäselväksi tai tuottanut vaikeuksia?
voimakkaimman signaalin ja sen poisto oli hieman hankala implementoida, koska siitä ei tunnu löytyvän hyvää materiaalia. Lopulta sain sen toimimaan. mutta en vieläkään ole aivan varma toimiiko se ihan oikein. Jos vahvimman signaalin suorittaa Testi3Siniaaltoja2.wav tiedostolle, niin se näyttää siltä, että se antaisi väärän tuloksen. Luulen kuitenkin, että tämä johtuu siitä, että kuvaan vain aidon osa datasta ja jätän imaginääridatan huomiotta, mutta vahvimman signaalin valitsiessani otan koko datan huomioon.

### Mitä teen seuraavaksi?
Viime viikolta jäi paljon tekemättä, joten jatkan niistä:

- Yhdistän visualisointi välilehdelle aanenprosessointi.py kuvaajien piirtämistä

- Laaja Dokumentaation läpikäynti ja uusinta

- Testauksen kirjottaminen aanenprosessointi.py

### Kuinka paljon käytin aikaa projektiin viikolla?
10h

## Viikkoraportti 6
### Mitä olen tehnyt viikolla?
- Viimeistelty käyttöliittymää
- Korjattu vika ifft toteutuksesta.
- 

### Miten projekti on edistynyt?
Kaikki käyttöliittymän välilehdet ovat valmiit
- visualisointi
 - kuvaaja
 - vertailu
- suodatus
 - voimakkain taajuus
 - valitse taajuus
- aloitus


Korjasin ifft toteutuksen.

### Mitä opin viikolla?
ifft vaattii jonkun näköisen skaalauksen. Huomasin, että ifft toteutukseni antaa merkittävästi liian suuria arvoja, kun vertailin toteutuksia vierekkäin. Selvisi, että ifft oli tähän mennessä aina palauttanut taulun, jossa jokainen arvo on taulukon pituuden verran kerrottuna liian suuri. Eli arvo*taulukonPituus. Löysin aiheesta [stackoverflow:ssa](https://stackoverflow.com/questions/48572647/recursive-inverse-fft), joka auttoi ratkaisemaan ongelmani.

Ilmeisesti fft ja ifft skaalaavat dataa taulun pituuden suhteen, joten data pitää skaalata takaisin oikean kokoiseksi, kun sen haluaa muuttaa wav muotoon. Skaalauksen voisi toteuttaa siististi kertomalla fft ja ifft 1/sqrt(taulunpituus), mutta tämä aiheuttaa ylimääräisiä välivaiheita, joten skaalaus yleensä toteuttaan vain ifft:n päässä. Tästä ei aiheudu ongelmia, koska fft:ssä on tärkeää arvojen relatiivinen koko.


### Mikä jäi epäselväksi tai tuottanut vaikeuksia?

### Mitä teen seuraavaksi?

### Kuinka paljon käytin aikaa projektiin viikolla?

# Projektiin käytetty aika yhteensä
## 55h
<!--
## Viikkoraportti pohja
### Mitä olen tehnyt viikolla?

### Miten projekti on edistynyt?

### Mitä opin viikolla?

### Mikä jäi epäselväksi tai tuottanut vaikeuksia?

### Mitä teen seuraavaksi?

### Kuinka paljon käytin aikaa projektiin viikolla?
-->
