from datetime import datetime

class Etudiant:

    liste_etudiants = []

    def __init__(self, p_numero_etudiant: str = "", p_nom_etudiant: str = "", p_programme_etudiant: str = "",
                 p_date_naissance: datetime = "", p_liste_cours_inscrit: list = None):
        """
        Constructeur de la classe Etudiant
        :param p_numero_etudiant: Le numéro de l'étudiant
        :param p_nom_etudiant: Le nom de l'étudiant
        :param p_programme_etudiant: Le programme de l'étudiant
        :param p_date_naissance: La date de naissance de l'étudiant
        :param p_liste_cours_inscrit: La liste des cours inscrit de l'étudiant
        """
        self._numero_etudiant = p_numero_etudiant
        self._nom_etudiant = p_nom_etudiant
        self.programme_etudiant = p_programme_etudiant
        self.date_naissance = p_date_naissance
        if p_liste_cours_inscrit is None:
            self.liste_cours_inscrit = []
        else:
            self.liste_cours_inscrit = p_liste_cours_inscrit

    @property
    def numero_etudiant(self):
        return self._numero_etudiant

    @numero_etudiant.setter
    def numero_etudiant(self, v_numero_etudiant):
        if len(v_numero_etudiant) == 8 and v_numero_etudiant.isnumeric():
            self._numero_etudiant = v_numero_etudiant
        else:
            raise ValueError("Le numéro de l'étudiant doit être composée de 8 chiffres !")

    @property
    def nom_etudiant(self):
        return self._nom_etudiant

    @nom_etudiant.setter
    def nom_etudiant(self, v_nom_etudiant):
        if len(v_nom_etudiant) <= 100 and v_nom_etudiant.isalpha():
            self._nom_etudiant = v_nom_etudiant
        else:
            raise ValueError("Le nom de l'étudiant doit être composée uniquement de lettres !")

    @classmethod
    def ajouter_etudiant(cls, nouveau_etudiant):
        """
        Ajoute un étudiant dans la liste des étudiants s'il n'y a pas de répétition de numéro d'étudiant
        :param nouveau_etudiant: Un étudiant qu'on désire ajouter
        :return: True si l'étudiant est ajouté
        """
        for etudiant in cls.liste_etudiants:
            if etudiant.numero_etudiant == nouveau_etudiant.numero_etudiant:
                raise ValueError("L'étudiant n'a pas été ajouté, il existe déjà !")
        else:
            cls.liste_etudiants.append(nouveau_etudiant)
            return True

    def age(self):
        """
        Calcule l'âge de l'étudiant
        :return: L'âge de l'étudiant
        """
        age = datetime.now().year - self.date_naissance.year
        if self.date_naissance.month > datetime.now().month:
            age = age - 1
            return age
        elif self.date_naissance.month == datetime.now().month:
            if self.date_naissance.day > datetime.now().day:
                age = age - 1
                return age
            else:
                return age
        else:
            return age

    def __str__(self):
        """
        Affiche les informations sur l'étudiant
        :return: Les informations de l'étudiant
        """
        return (f"Numéro de l'étudiant : {self._numero_etudiant}\n"
                f"Nom de l'étudiant : {self._nom_etudiant}\n"
                f"Âge de l'étudiant : {self.age()} ans\n")
