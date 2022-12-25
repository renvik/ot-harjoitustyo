## Viikko 3
- Tehty yksinkertainen graafinen käyttöliittymä, jolla voi hakea junan tietoja sen numeron perusteella
- rajapintayhteys on toteutettu niin että tiedot tulostuvat terminaaliin, seuraavassa versiossa ne tulostetaan käyttöliittymään.
- Lisätty Trainrepository-luokka, joka vastaa tietojen hausta rajapinnasta
- Lisätty TrainService-luokka, joka ohjaa Trainrepository-luokkaa
- Asennettu pytest, tehty runko testaukseen käytettävään tiedostoon, varsinainen testi kuitenkin puuttuu vielä
## Viikko 4
- Tehty pakkauskaavio
- Rajapinnan vastauksen tietojen näyttäminen graafisessa käyttöliittymässä (ei toimi vielä)
- Lisätty testi rajapintaan (joka ei myöskään toimi vielä)
- Lisätty invoken taskeja
- päivitetty dokumentaatio, lisätty arkkitehtuuri.md
## Viikko 5
- testi jolla voi testata, että rajapinta palauttaa statuksen 200 toimii nyt
- vastaustietojen näyttäminen graafisessa käyttöliittymässä ei toimi vieläkään, tähän myös kysytty apua ohjaajilta 
- päivitetty dokumentaation, lisätty sekvenssikaavioarkkitehtuuriin.
## Viikko 6
- käyttöliittymät refaktoroitu: ui ohjaa nyt käyttöliittymäluokkia SearchView ja ResultsView
- SearchView:stä pääsee siirtymään ResultsView-näkymään johon tällä hetkellä tulostuu placeholder -teksti
- rajapintahaun tiedot tulostuu yhä terminaaliin
- dokumentaatio: arkkitehtuurikuvaus, käyttöohje yms. päivitetty
## Viikko 7
- junatietojen haussa voi antaa nyt päivämäärän (aiemmin kovakoodattu tähän päivään)
- dokumentaatio päivitetty vastaamaan lopullista toiminnallisuutta
