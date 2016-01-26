Kuntien ostolaskujen avaamisohje (DRAFT)
========================================

Versio 0.3, päivitetty 1.12.2015 klo 16:00.

HUOM: tämä ei ole vielä lopullinen versio. Katso kommentointiohje alta.

Nämä ohjeet on tehty Kuutoskaupunkien (Helsinki, Espoo, Vantaa, Tampere,
Turku ja Oulu) ja Kuntaliiton yhteistyönä.
Ohjeiden pohjana on käytetty kuntien jo avaamaa ostolaskudataa ja hyödynnetty
myös kansainvälistä OCDS-standardia
http://ocds.open-contracting.org/standard/r/1__0__RC/en/schema/reference/#transaction.

Kun avaat ostolaskuja, julkaise myös kuntasi tililuettelo ja tilien kirjausohje.
Näin aineiston hyödyntäjä ymmärtää paremmin, mistä eri kentissä on kyse.
Ostolaskut kannattaa avata koneluettavassa ja valmistajariippumattomassa CSV-tiedostomuodossa. 
Tämän lisäksi ne voi avata esimerkiksi Excel-muodossa.

Voit kommentoida tätä ohjetta Githubissa tai lähettämällä kommentit
sähköpostilla osoitteeseen aapo.rista at forumvirium.fi. 
Kommenttien ja palautteen perusteella ohjetta parannetaan.

Ostolaskun avaajan askelet
--------------------------

Poista aineistosta yksityisten elinkeinonharjoittajien eli 
ns. toiminimiyrittäjien laskut. Toiminimet ovat yleensä luonnollisia henkilöitä, 
ja niiden julkaiseminen saattaa johtaa henkilörekisterin muodostumiseen.
Siksi tässä vaiheessa on varminta poistaa ne aineistosta. 
Asiasta on pyydetty lausuntoa tietosuojavaltuutetulta. 
Kun se saadaan, päivitämme ohjeen ja ilmoitamme asiasta.

Varmista, että ostolaskuaineistossa on vähintään tässä ohjeessa mainitut kentät.
Kaikki lisätiedot on tervetulleita, joten mitään ei kannata suodattaa pois
siksi, että sitä ei ole tässä ydinvalikoimassa mainittu.

Julkaise kentät samassa järjestyksessä kuin tässä ohjeessa. 
Mikäli julkaistavassa aineistossa on enemmän tietoja kuin ydinvalikoimassa,
järjestä kentät taulukon loppuun.
Jos johonkin kenttään ei löydy tietoa, jätä se tyhjäksi.
Käytä ainoastaan yhtä otsikkoriviä ja aloita laskudata suoraan riviltä 2.
Esimerkki: https://goo.gl/luok3l 

Lisensoi aineiston käyttö Creative Commons 4.0 -lisenssillä (CC BY 4.0):
https://creativecommons.org/licenses/by/4.0/legalcode.fi 
Lisenssi antaa käyttäjälle luvan käyttää aineistoa vapaasti,
kunhan mainitsee lähteen.

Pakolliset kentät
-----------------

* Kuntakoodi
* Kunnan nimi
* Ostajan Y-tunnus
* Tulosyksikön ID (esim. virasto tai muu yksikkö)
* Tulosyksikön nimi
* Osasto (jos sellainen on, esim. sote)
* Kustannuspaikan ID
* Kustannuspaikan nimi
* Laskun päivämäärä (laskusta)
* Tositteen numero (kirjanpitojärjestelmässä)
* Ostotilausnumero
* Sopimusnumero
* Kirjauspäivämäärä
* Laskun numero (alkuperäinen numero kuten se on laskussa esiintynyt)
* Tiliryhmän numero (esim. 430, katso Kuntaliiton tililuettelomalli) 
* Tiliryhmän nimi (esim. Palvelujen ostot)
* Tilin numero (esim. 4422)
* Tilin nimi (esim. Kuljetukset ja konepalvelut)
* Toimittajan nimi
* Toimittajan Y-tunnus
* Summa ALV0 euroina
* ALVin määrä euroina
* Kokonaissumma euroina

Vapaaehtoiset kentät
--------------------

* Verkkolaskuosoite
* Tilausnumero
* Toimittajan numero
* Kumppaniyhtiö (Helsinki)
  * Kumppanin id
  * Kumppanin selkokielinen nimi
* Kumppaniryhmä (Helsinki)
  * Esim. sisäinen vai ulkoinen osto
  * Tarkempi erittely: tytäryhtiöt ja säätiöt, valtio jne.
  * Kumppaniryhmän selkokielinen nimi

