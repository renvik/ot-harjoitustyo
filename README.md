# Train information
Sovelluksen avulla käyttäjä voi hakea Suomen raideliikenteeseen liittyvää tietoa, jonka lähteenä on Fintrafficin tarjoama REST-rajapinta. Sovelluksen käyttö ei vaadi rekisteröitymistä eikä sovelluksen kautta tehdyt kyselyjä tai niiden tuloksia tallenneta.
## Python-versio
Sovellus on testattu vain Python-versiolla 3.8. Sovellus ei välttämättä toimi oikein vanhemmilla versioilla.
## Dokumentaatio
- [Vaatimusmaarittely](https://github.com/renvik/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuuri](https://github.com/renvik/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](https://github.com/renvik/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/renvik/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
- [Testaus](https://github.com/renvik/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md)
- [Release](https://github.com/renvik/ot-harjoitustyo/releases/tag/loppupalautus)

## Asennus

1. Riippuvuuksien asentaminen

```bash
poetry install
```
2. Tarvittavien riippuvuuksien asentaminen

```bash
poetry run invoke build
```

3. Sovelluksen käynnistäminen

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman voi suorittaa komennolla: 

```bash
poetry run invoke start
```
### Testaus

Testit tehdään komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti luodaan seuraavasti:

```bash
poetry run invoke coverage-report
```

Raportti luodaan _htmlcov_-hakemistoon.


### Pylint
.pylintrc:ssä määritellyt tarkistukset suoritetaan komennolla:

```bash
poetry run invoke lint
```
