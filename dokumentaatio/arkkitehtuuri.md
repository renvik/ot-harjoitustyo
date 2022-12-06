# Arkkitehtuurikuvaus

## Pakkausrakenne
![repository pattern and classes](https://user-images.githubusercontent.com/51605816/204633015-bcce8070-784a-41b7-a923-ed2847af087e.png)

## Päätoiminnallisuudet
### Juna-tiedon hakeminen junan numeron perusteella
Käyttäjä voi hakea tietoa tietystä junasta antamalla kyseisen junan numeron. Kun syötekenttään kirjoitetaan junan numero ja klikataan painiketta _Search_, etenee sovelluksen kontrolli seuraavasti:
![sekvenssikaavio](https://user-images.githubusercontent.com/51605816/205909906-232b3e40-fd40-4b3c-aef2-e100819c8123.png)
Painikkeen painamiseen reagoiva tapahtumankäsittelijä kutsuu sovelluslogiikan `TrainService` metodia antaen parametriksi junan numeron. Sovelluslogiikka hakee `TrainRepository`:n avulla rajapinnasta junannumeron perusteella kyseisen junan tiedot. Tämän jälkeen käyttöliittymä näyttää junan tiedot. 

