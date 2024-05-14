from Classes.Classe_Etudiant import Etudiant

class Local:
    liste_locaux = []

    def __init__(self, p_type_local: str = "", p_numero_local: str = "", p_lieu_local: str = "",
                 p_superficie_local: float = 0.0, p_nombre_places: int = 0, p_liste_etudiants: list[Etudiant] = None):
        """
        Constructeur de la classe local
        :param p_type_local: Le type de local
        :param p_numero_local: Le numéro du local
        :param p_lieu_local: Dans quel bloc se situe le local [A/B/C]
        :param p_superficie_local: La superficie du local en mètres carrés
        :param p_nombre_places: Le nombre de places du local
        :param p_liste_etudiants: La liste des étudiants dans ce local
        """
        self._numero_local = p_numero_local
        self._superficie_local = p_superficie_local
        self._nombre_places = p_nombre_places
        self.type_local = p_type_local
        self.lieu_local = p_lieu_local
        if p_liste_etudiants is None:
            self.liste_etudiants = []
        else:
            self.liste_etudiants = p_liste_etudiants

    @property
    def numero_local(self):
        return self._numero_local

    @numero_local.setter
    def numero_local(self, v_numero_local):
        if isinstance(v_numero_local, str) and len(v_numero_local) == 5 and v_numero_local[0].isalpha() and v_numero_local[1] == "-" and v_numero_local[2:].isnumeric():
            self._numero_local = v_numero_local
        else:
            raise ValueError("Le numéro du local est composé de 5 caractères ! Le premier est une lettre, le deuxième un tiret et le reste des chiffres !")

    @property
    def superficie_local(self):
        return self._superficie_local

    @superficie_local.setter
    def superficie_local(self, v_superficie_local):
        if isinstance(v_superficie_local, float) and v_superficie_local > 0:
            self._superficie_local = v_superficie_local
        else:
            raise ValueError("La superficie du local doit être un nombre positif !")

    @property
    def nombre_places(self):
        return self._nombre_places

    @nombre_places.setter
    def nombre_places(self, v_nombre_places):
        if isinstance(v_nombre_places, int) and 0 < v_nombre_places < 25:
            self._nombre_places = v_nombre_places
        else:
            raise ValueError("Le nombre de places doit être un nombre entier positif inférieur à 25 !")

    @classmethod
    def ajouter_local(cls, nouveau_local):
        """
        Ajoute un nouveau local dans la liste des locaux
        :param nouveau_local: Le nouveau local
        :return: True si l'ajout passe
        """
        for local in cls.liste_locaux:
            if local.numero_local == nouveau_local.numero_local:
                raise ValueError("Ce local existe déjà !")
        else:
            cls.liste_locaux.append(nouveau_local)
            return True

    def __str__(self):
        """
        Affiche les informations sur le local
        :return: Les informations sur le local
        """
        return (f"Le numéro du local : {self._numero_local}\n"
                f"La superficie du local : {self._superficie_local} mètres carrés\n"
                f"Le nombre de places : {self._nombre_places}\n"
                f"Le type de local : {self.type_local}\n"
                f"Lieu du local : Bloc {self.lieu_local}\n")