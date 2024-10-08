## Secret Santa-skripti

Hyvin simppeli secret santa-arvonta pythonkapula.

### Mitä tämä tekee?
- Arpoo satunnaisesti, kenelle kukin ostaa lahjan.
- Voidaan huomioida mahdolliset rajoitukset (esim. jos joku ei voi ostaa lahjaa tietylle henkilölle).
- Lähettää sähköpostit osallistujille, joissa kerrotaan, kenelle heidän pitää ostaa lahja.
### Miten käytän tätä?
Asenna:

1. Varmista, että Python asennettuna (versio 3 tai uudempi).

2. Lisää osallistujat:

#### Luo tiedosto nimeltä participants.json ja lisää sinne osallistujien tiedot seuraavasti:

```
[
  {
    "name": "Matti",
    "email": "matti@example.com",
    "constraints": ["Maija"]
  },
  {
    "name": "Maija",
    "email": "maija@example.com",
    "constraints": []
  },
  {
    "name": "Teppo",
    "email": "teppo@example.com",
    "constraints": []
  }
]
```
<br>
3. Aseta sähköpostiasetukset:

- Skripti käyttää sähköpostien lähettämiseen Gmailia. Tarvitset sovellussalasanan.

- Mene Google-tilisi asetuksiin ja ota käyttöön kaksivaiheinen tunnistus.
Luo sovellussalasana ja käytä sitä.
4. Aseta ympäristömuuttujat:
```
Linux/macOS:
export SMTP_USERNAME='oma.sahkoposti@gmail.com'
export SMTP_PASSWORD='sovellussalasanasi'

Windows:
set SMTP_USERNAME=oma.sahkoposti@gmail.com
set SMTP_PASSWORD=sovellussalasanasi
```
<br>
5. Suorita arvonta:

```
python draw_secret_santa.py
```
<br>
6. Lähetä sähköpostit:

```
python send_emails.py
```

### Huomioita
Testaa ennen lähetystä: Kannattaa testata skriptiä ennen kuin lähetät oikeita sähköposteja.
Yksityisyys: Muistahan käsitellä kavereiden tietoja huolella :)