# Käyttöohje

## Ohjelman käynnistäminen

Asenna ensin riippuvuudet komennolla:

```bash
poetry install
```

Suorita sitten alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Lopuksi käynnistä ohjelma komennolla:

```
poetry run invoke start
```

## Junatietojen hakeminen

Voit hakea junaan liittyviä tietoja syöttämällä junan numero lomakekkeen tekstikenttään ja painamalla painiketta Search. 
Junan tiedot näytetään erillisessä näkymässä. Kun erillinen näkymä suljetaan niin palataan lomakenäkymään. Ohjelma lopetetaan sulkemalla lomakenäkymä
