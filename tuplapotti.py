import random
import json

def is_valid(giver, receiver, assignment):
    # Tarkistetaan, ettei antaja ja saaja ole sama henkilö
    if giver['name'] == receiver['name']:
        return False
    # Tarkistetaan, ettei saajaa ole jo valittu toiselle antajalle
    if receiver['name'] in assignment.values():
        return False
    # Tarkistetaan antajan mahdolliset rajoitukset
    if receiver['name'] in giver.get('constraints', []):
        return False
    return True

def assign_giftees(participants):
    assignment = {}
    receivers = participants.copy()
    random.shuffle(receivers)

    for giver in participants:
        # Etsitään kelvolliset saajat antajalle
        valid_receivers = [r for r in receivers if is_valid(giver, r, assignment)]
        if not valid_receivers:
            return None  # Jos ei löydy kelvollista saajaa, palautetaan None
        # Valitaan satunnainen saaja kelvollisten joukosta
        receiver = random.choice(valid_receivers)
        assignment[giver['name']] = receiver['name']
        receivers.remove(receiver)  # Poistetaan valittu saaja listalta
    return assignment

def find_valid_assignment(participants):
    attempts = 0
    while attempts < 1000:
        assignment = assign_giftees(participants)
        if assignment:
            return assignment  # Kelvollinen paritus löytyi
        attempts += 1
    raise Exception("Arvontaa ei voitu suorittaa onnistuneesti.")

def main():
    # Ladataan osallistujatiedot tiedostosta
    with open('participants.json', 'r', encoding='utf-8') as f:
        participants = json.load(f)

    # Suoritetaan arvonta
    assignment = find_valid_assignment(participants)

    # Tallennetaan arvonnan tulokset tiedostoon
    with open('arvotut.json', 'w', encoding='utf-8') as f:
        json.dump(assignment, f, ensure_ascii=False, indent=4)

    print("Arvonta suoritettu ja tulokset tallennettu tiedostoon 'arvotut.json'.")
    print("Voit tarkastella tiedostoa kehitysvaiheessa. Lopullisessa käytössä vältä katsomasta tiedoston sisältöä. Pysyy yllätys yllä :)")

if __name__ == "__main__":
    main()
