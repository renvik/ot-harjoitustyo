# Testausdokumentti
### Sovelluslogiikka
Pyrin testaamaan sovelluslogiikasta vastaavaa `TrainService`-luokkaa. TrainService -olio alustettiin niin, että sille injektoidaan riippuvuudeksi 
TrainRepository -olio. Tarkoitus oli testata rajapintayhteyden toimivuutta niin, että lähetetään kutsu rajapintaan ja tarkistetaan tuleeko vastauksessa
status-koodi 200. Tähän liittyen sain ohjaajalta palautetteen, että ei ole tarkoitus testata ulkoista palvelua kuten rajapintaa, joten poistin testin.
Muuta testiä en osannut tehdä.
### Asennus ja konfigurointi
Tein sovelluksesta releasen ja testasin sen asentamista Cubbli-ympäristössä. Poetry install -komento aiheutti kuitenkin "does not contain any element" 
-virheilmoituksen enkä tiedä, mistä se johtuu.
