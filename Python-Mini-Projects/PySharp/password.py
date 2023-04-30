import os

# k = key
# kc = key_char
# m = message
# ec = encrypted
# ec_c = encrypted_char

OFFSET = 0b10101010
def encrypt(k, m):
    if not k or not m:
        raise ValueError("Paramètres invalides")

    key = [ord(c) % 256 for c in k]

    ec = []
    for i, c in enumerate(m):
        kc = key[i % len(key)]
        ec_c = chr(((ord(c) + kc) * (i + 1)) ^ ((i + 1) * OFFSET))
        ec.append(ec_c)

    return "".join(ec)

# dc = decrypted
# dc_c = decrypted_chars

def decrypt(k, e):
    if not k or not e:
        raise ValueError("Paramètres invalides")
    
    key = [ord(c) for c in k]

    dc = []
    for i, c in enumerate(e):
        kc = key[i % len(key)]
        dc_c = chr(((ord(c) ^ ((i + 1) * OFFSET))) // (i + 1) - kc)
        dc.append(dc_c)
    
    return "".join(dc)
  
def afficher_passwords():
    with open("messages.txt", "r", encoding="utf-8") as file:
        data = file.read()
        if data.strip():
            print(data)
        else:
            print("Aucun message n'a été trouvé\n")

if __name__ == "__main__":
    while True:
        os.system("cls")
        choix = input("1. Chiffrer | 2. Déchiffrer | 3. Afficher mots de passe | 4. Quitter\nQue souhaitez-vous faire ? \n\n\x1b[?25l")
        os.system("cls")
        if choix  == "1":
            key = "\/x1d|u/\/x0f~<uO2/\/n{"
            titre = input("Entrez le titre : ")
            msg = input("Entrez votre mot de passe : ")

            encrypted = encrypt(key, msg)
            with open("messages.txt", "a", encoding="utf-8") as file:   
                file.write(f"Jeu / Application: {titre} \nMot de passe: {repr(encrypted)}\n\n")

            print("\nPlus d'Information","\nMot de passe chiffré :", repr(encrypted),"\n")
            print("Appuyer sur une touche pour continuer.\x1b[?25l")
            os.system("pause >nul")
        elif choix  == "2":
            key = "\/x1d|u/\/x0f~<uO2/\/n{"
            password = input("Entrez le mot de passe chiffré : ")
            decrypted_password = decrypt(key, password)
            print(f"Le mot de passe déchiffré est : {decrypted_password}\n")
            print("Appuyer sur une touche pour continuer.\x1b[?25l")
            os.system("pause >nul")
        elif choix  == "3":
            afficher_passwords()
            print("Appuyer sur une touche pour continuer.\x1b[?25l")
            os.system("pause >nul")
        elif choix  == "4":
            print("Au revoir !\x1b[?25l")
            os.system("pause >nul")
            break
        else:
            print("Veuillez répondre 'Chiffrer', 'Déchiffrer', 'Afficher mots de passe' ou 'Quitter'.")
            os.system("pause")
