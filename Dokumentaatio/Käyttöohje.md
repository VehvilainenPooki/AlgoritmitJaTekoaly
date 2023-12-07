# Käyttöohje
1. Lataa repositorio.
2. Luo python venv repositorion juureen.
3. aktivoi venv.
4. asenna requirement.txt.
5. navigoi Koodi kansioon
6. Suorita kayttoliittyma.py

# Käyttöliittymä
## Valikko
Ruudun yläreunasta löydät valikon, jolla voit navigoida eri välilehtien välillä.
### Aloitusruutu
Aloitusruutu on aloitusruutu. Sieltä löytyy linkki tähän tiedostoon.
### Visualisointi
#### Kuvaaja
Kuvaajaruudulla voit tarkastella yhden tiedoston kuvaajia erinäisillä toiminnoilla:
- FFT toteutus määrää käytetäänkö minun totetuttamaa algoritmia vai SciPy.IO kirjaston paljon tehokkaampaa versiota.
- Suoritetaanko FFT/iFFT määrää suoritetaanko niitä.
 - Ilman kumpaakin kuvataan vain tiedoston ääni.
 - FFT antaa taajuusspektrin tiedostolle.
 - iFFT ei ole mitään järkeä suorittaa yksin.
 - FFT + iFFT palaa takaisin alkuperäiseen ääneen.

#### Vertaile
Vertaileruudulla pystyy vertailemaan FFT toteutuksia tai kahta eri tiedostoa.
FFT vertailusta huomaa, että toetukset eivät anna aivan samoja arvoja, mutta hyvin lähes samat.
Tiedostoja voi vertailla sen jälkeen, kun on muokannut jostakin tiedostosta dataa pois.

### Suodatus
#### Voimakkain taajuus
Voimakkain taajuusruudussa voit nähdä ja poistaa voimakkaimman taajuuden. Tällä sivulla on kuvaaja muutettu itseisarvoiseen muotoon, jotta siitä näkyy myös imaginäärilukujen vaikutus arvoon.

#### Valitse taajuus
Tällä sivulla voi poistaa haluamansa taajuuden.