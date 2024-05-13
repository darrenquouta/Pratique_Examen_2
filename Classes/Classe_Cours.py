from Classes.Classe_Etudiant import Etudiant

class Cours:
    liste_cours = []

    def __init__(self, p_sigle_cours: str = "", p_titre_cours: str = "", p_nombre_heures_cours: int = 0,
                 p_liste_etudiants_inscrits: list[Etudiant] = None):
        """
        Constructeur de la classe Cours
        :param p_sigle_cours: Le sigle du cours
        :param p_titre_cours: Le titre du cours
        :param p_nombre_heures_cours: Le nombre d'heures de cours
        :param p_liste_etudiants_inscrits: La liste des étudiants inscrits au cours
        """
        self._sigle_cours = p_sigle_cours
        self._titre_cours = p_titre_cours
        self._nombre_heures_cours = p_nombre_heures_cours
        if p_liste_etudiants_inscrits is None:
            self.liste_etudiants_inscrits = []
        else:
            self.liste_etudiants_inscrits = p_liste_etudiants_inscrits

    @property
    def sigle_cours(self):
        return self._sigle_cours

    @sigle_cours.setter
    def sigle_cours(self, v_sigle_cours):
        if isinstance(v_sigle_cours, str) and len(v_sigle_cours) == 5 and v_sigle_cours[0].isalpha() and v_sigle_cours[1:].isnumeric():
            self._sigle_cours = v_sigle_cours
        else:
            raise ValueError("Le sigle du cours doit être de cinq caractères ! Le premier un caractère alphabétique et les autres numériques !")

    @property
    def titre_cours(self):
        return self._titre_cours

    @titre_cours.setter
    def titre_cours(self, v_titre_cours):
        if isinstance(v_titre_cours, str) and len(v_titre_cours) <= 60:
            self._titre_cours = v_titre_cours
        else:
            raise ValueError("Le titre du cours ne doit pas dépasser 60 caractères !")

    @property
    def nombre_heures_cours(self):
        return self._nombre_heures_cours

    @nombre_heures_cours.setter
    def nombre_heures_cours(self, v_nombre_heures_cours):
        if isinstance(v_nombre_heures_cours, int) and 0 < v_nombre_heures_cours <= 12:
            self._nombre_heures_cours = v_nombre_heures_cours
        else:
            raise ValueError("Le nombre d'heures de cours doit être un nombre entier supérieur à 0 et inférieur à 12 !")

    @classmethod
    def ajouter_cours(cls, nouveau_cours):
        """
        Ajoute un nouveau cours dans la liste des cours si son sigle est unique
        :param nouveau_cours: Un nouveau cours
        :return: True s'il est ajouté, False sinon
        """
        for cours in cls.liste_cours:
            if cours.sigle_cours == nouveau_cours.sigle_cours:
                return False
        else:
            cls.liste_cours.append(nouveau_cours)
            return True

    def __str__(self):
        """
        Affiche les informations sur le cours
        :return: Les informations sur le cours
        """
        return (f"Sigle du cours : {self._sigle_cours}\n"
                f"Titre du cours : {self._titre_cours}\n"
                f"Nombre d'heures de cours : {self._nombre_heures_cours}\n")
