import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main():
    # Ladataan osallistujatiedot
    with open('participants.json', 'r', encoding='utf-8') as f:
        participants = json.load(f)

    # Luodaan sanakirja osallistujista nimien perusteella
    participants_dict = {p['name']: p for p in participants}

    # Ladataan arvonnan tulokset
    with open('arvotut.json', 'r', encoding='utf-8') as f:
        assignment = json.load(f)

    # SMTP-palvelimen asetukset
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SMTP_USERNAME = '@gmail.com'
    SMTP_PASSWORD = "xxxx-xxxx-xxxx-xxxx" 

    # Lähetetään sähköpostit
    for giver_name, receiver_name in assignment.items():
        giver = participants_dict[giver_name]
        receiver = participants_dict[receiver_name]
        recipient_email = giver['email']
        subject = 'Secret Santa - Lahjansaajasi'

        # HTML-sähköpostipohja, johon kuva on lisätty
        html_body = f"""<html>
<body style="font-family: 'Arial', sans-serif; color: #333; background-color: #f9f9f9; padding: 20px;">
  <div style="max-width: 600px; margin: 0 auto; background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    <div style="text-align: center;">
      <!-- Lisätään kuva tähän -->
      <img src="https://i.postimg.cc/8PXb7qW8/photo.jpg" alt="Joulukuva" style="max-width: 100%; height: auto; border-radius: 10px; margin-bottom: 20px;">
    </div>
    <h1 style="color: #b22222; text-align: center;">🎅 Secret Santa 🎅</h1>
    <p style="font-size: 16px; text-align: center; color: #4b4b4b;">
      Hei <strong>{giver['name']}</strong>,<br><br>
      Pikkujoulut lähestyvät... <br> <br> Tontut ovat arponeet, ja sinut on valittu ostamaan lahja henkilölle <strong>{receiver['name']}</strong> 🎁
    </p>
    <p style="text-align: center;">
      Ole luova ja yllätä hänet jollakin, mistä hän pitää!<br><br>
      Budjetti: 20€<br>
      Nähdään pikkujouluissa<br>
      <em>t. tontut 🎄</em>
    </p>
    <footer style="text-align: center; margin-top: 20px; font-size: 9px; color: #777;">
      © 2024 kiusa-t. Valitukset tontuille osoitteeseen <a href="https://santaclausvillage.info/">santaclausvillage.info</a>.
    </footer>
  </div>
</body>
</html>"""

        # Luodaan MIMEMultipart-objekti
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email

        # Lisätään HTML-sisältö viestiin
        msg.attach(MIMEText(html_body, 'html'))

        try:
            # Lähetetään sähköposti
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.ehlo()  # Tervehditään palvelinta
                server.starttls()  # Aloitetaan TLS-salaus
                server.ehlo()  # Tervehditään uudelleen salatun yhteyden yli
                server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Kirjaudutaan sisään
                server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())  # Lähetetään viesti
            print(f"Sähköposti lähetetty: {giver['name']} -> {recipient_email}")
        except Exception as e:
            print(f"Virhe lähettäessä sähköpostia osoitteeseen {recipient_email}: {e}")

    print("Kaikki sähköpostit on lähetetty.")

if __name__ == "__main__":
    main()
