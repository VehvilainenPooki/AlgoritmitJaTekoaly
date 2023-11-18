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


# Projektiin käytetty aika yhteensä
## 25h
<!--
## Viikkoraportti pohja
### Mitä olen tehnyt viikolla?

### Miten projekti on edistynyt?

### Mitä opin viikolla?

### Mikä jäi epäselväksi tai tuottanut vaikeuksia?

### Mitä teen seuraavaksi?

### Kuinka paljon käytin aikaa projektiin viikolla?
-->
