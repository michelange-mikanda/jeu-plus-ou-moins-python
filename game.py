python
import random

def jeu_plus_ou_moins():
    """
    Un jeu simple où le joueur doit deviner un nombre secret entre 1 et 100.
    Cette version améliorée inclut un compteur de tentatives et une limite de difficulté.
    """
    print("\n" + "="*50)
    print("===      JEU DU PLUS OU MOINS (Devine le nombre !)      ===")
    print("="*50 + "\n")
    print("J'ai choisi un nombre secret entre 1 et 100.")
    print("Tu as 10 tentatives pour le trouver. Bonne chance !\n")

    nombre_secret = random.randint(1, 100)
    nombre_tentatives = 0
    limite_tentatives = 10

    while nombre_tentatives < limite_tentatives:
        try:
            tentative_str = input(f"➡️  Tentative n°{nombre_tentatives + 1}/{limite_tentatives}. Entre un nombre : ")
            tentative = int(tentative_str)
        except ValueError:
            print("❌ ERREUR : Ce n'est pas un nombre valide. Essaie encore.")
            continue

        nombre_tentatives += 1

        if tentative < 1 or tentative > 100:
            print("⚠️ ATTENTION : Le nombre doit être entre 1 et 100.")
        elif tentative < nombre_secret:
            print("C'est plus ! ⬆️")
        elif tentative > nombre_secret:
            print("C'est moins ! ⬇️")
        else:
            print(f"\n🎉 BRAVO ! Tu as trouvé le nombre secret '{nombre_secret}' en {nombre_tentatives} tentatives !")
            return

    print(f"\n GAME OVER 😞 Tu as épuisé tes {limite_tentatives} tentatives. Le nombre secret était {nombre_secret}.")
    print("-" * 50 + "\n")

if __name__ == "__main__":
    jeu_plus_ou_moins()
    