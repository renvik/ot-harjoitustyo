# Arkkitehtuurikuvaus

## Pakkausrakenne
Rakenteessa on erotettu toisistaan eri kerrokset: ui, services ja repositories. Ui vastaa käyttöliittymästä, services logiikasta ja repositories tietojen hausta ja muokkauksesta.
![repository pattern and classes](https://user-images.githubusercontent.com/51605816/204633015-bcce8070-784a-41b7-a923-ed2847af087e.png)

## Käyttöliittymä
Käyttöliittymä koostuu kahdesta näkymästä: hakutietojen syöttölomake ja hakutulosten näyttäminen. Vain yksi näkymä voi näkyä kerrallaan ja ne ovat eri luokissa. Näkymien luokissa ei ole varsinaista ohjelmalogiikka vaan ne kutsuvat TrainService-luokan metodeja.

## Sovelluslogiikka
Logiikasta vastaa luokan TrainService olio ja luokka tarjoaa käyttöliittymälle metodin 

- `get_train(self, train_number)`

TrainServicen saa käyttöönsä junatiedot repositories sijaitsevan luokan TrainRepository kautta.

## Tietojen tallennus
Sovellus ei tallenna käyttäjän tekemiä hakuja eikä niiden tuloksia.

## Päätoiminnallisuudet
### Juna-tiedon hakeminen junan numeron perusteella
Käyttäjä voi hakea tietoa tietystä junasta antamalla kyseisen junan numeron. Kun syötekenttään kirjoitetaan junan numero ja klikataan painiketta _Search_, etenee sovelluksen kontrolli seuraavasti:
![sekvenssikaavio](https://user-images.githubusercontent.com/51605816/205909906-232b3e40-fd40-4b3c-aef2-e100819c8123.png)

Painikkeen painamiseen reagoiva tapahtumankäsittelijä kutsuu sovelluslogiikan `TrainService` metodia antaen parametriksi junan numeron. Sovelluslogiikka hakee `TrainRepository`:n avulla rajapinnasta junannumeron perusteella kyseisen junan tiedot. Tämän jälkeen käyttöliittymä näyttää junan tiedot. 

## Ohjelman rakenteeseen jääneet heikkoudet

