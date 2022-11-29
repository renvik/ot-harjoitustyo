# Train information
Sovelluksen avulla käyttäjä voi hakea raideliikenteeseen liittyvää tietoa, jonka lähteenä on Fintrafficin tarjoama REST-rajapinta. Sovelluksen käyttö ei vaadi rekisteröitymistä.
## Python-versio
Sovellus on testattu vain Python-versiolla 3.8. Sovellus ei välttämättä toimi oikein vanhemmilla versioilla.
## Dokumentaatio
[vaatimusmaarittely.md](https://github.com/renvik/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
[arkkitehtuuri.md](https://github.com/renvik/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
[työaikakirjanpito.md](https://github.com/renvik/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
[changelog.md](https://github.com/renvik/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

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

### Pylint
.pylintrc:ssä määritellyt tarkistukset suoritetaan komennolla:

```bash
poetry run invoke lint
```
