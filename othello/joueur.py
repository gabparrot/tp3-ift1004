from random import choice


class Joueur:
    """
    Classe générale de joueur. Vous est fournie.
    """

    def __init__(self, couleur):
        """
       Le constructeur global de Joueur.

       Args:
           couleur: La couleur qui sera jouée par le joueur.

       Returns:
           La couleur "noir" ou "blanc" du joueur
       """
        assert couleur in ["blanc", "noir"], "Piece: couleur invalide."

        self.couleur = couleur

    def obtenir_type_joueur(self):
        """
        Cette méthode sera utilisée par les sous-classes JoueurHumain et
        JoueurOrdinateur.

        Returns:
            Le type de joueur, 'Ordinateur' ou 'Humain'
        """
        pass

    def choisir_coup(self, coups_possibles):
        """
        Cette méthode sera implémentée par les sous-classes JoueurHumain et
        JoueurOrdinateur.

        Args:
            coups_possibles: la liste des coups possibles

        Returns:
            un couple (ligne, colonne) représentant la positon du coup désiré.
        """
        pass


class JoueurHumain(Joueur):
    """
    Classe modélisant un joueur humain.

        Args:
            Le joueur humain.

        Returns:
            La modélisation du joueur humain.
    """

    def __init__(self, couleur):
        """
        Cette méthode va construire un objet Joueur et l'initialiser avec la
        bonne couleur.

        Args:
            La coulour du joueur.

        Returns:
            Objet Joueur de la bonne couleur.
        """
        super().__init__(couleur)

    def obtenir_type_joueur(self):
        return "Humain"

    def choisir_coup(self, coups_possibles):
        """
        Demande successivement à l'usager à quelle ligne, puis à quelle
        colonne il désire jouer.

        Args:
            coups_possibles: Le dictionnaire des coups possibles

        Returns:
            un couple (ligne, colonne) représentant la position du coup désiré.
        """
        try:
            input_row = int(input("Sur quelles lignes (0 à 7) voulez vous "
                                  "jouer votre coup? "))
            input_col = int(input("Et sur quelle colonne? (0 à 7) "))
            return input_row, input_col

        except ValueError:
            print("Position invalide.\n\n")
            # Si usager fait entree invalide, on retourne tuple hors planche
            # Ceci forcera le programme à redemander le coup au joueur.
            return -1, -1


class JoueurOrdinateur(Joueur):
    """
    Classe modélisant un joueur Ordinateur.

        Args:
            La couleur du joueur Ordinateur

        Returns:
            La modélisation du joueur Ordinateur
    """
    def __init__(self, couleur):
        """
        Cette méthode va construire un objet Joueur et l'initialiser avec la
        bonne couleur.

        Args:
            La coulour du joueur

        Returns:
            Objet Joueur de la bonne couleur
        """
        super().__init__(couleur)

    def obtenir_type_joueur(self):
        return "Ordinateur"

    def choisir_coup(self, coups_possibles):
        """
        Intelligence artificielle du joueur ordinateur.

        Args:
            coups_possibles: Le dictionnaire des coups possibles

        Returns:
            un couple (ligne, colonne) représentant la position du coup désiré.
        """
        if len(coups_possibles) == 0:
            return -1, -1
        else:
            return choice(coups_possibles)