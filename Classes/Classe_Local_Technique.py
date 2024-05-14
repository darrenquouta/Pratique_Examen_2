from Classes.Classe_Local import Local
from Classes.Classe_Etudiant import Etudiant

class Local_Technique(Local):

    def __init__(self, p_type_local: str = "", p_numero_local: str = "", p_lieu_local: str = "",
                 p_superficie_local: float = 0.0, p_nombre_places: int = 0, p_liste_etudiants: list[Etudiant] = None,
                 p_marque_ordinateurs: str = "", p_nombre_ordinateurs: int = 0, p_projecteur: bool = False):
        """
        Constructeur de la classe Local_Technique
        :param p_type_local: Le type de local
        :param p_numero_local: Le numéro du local
        :param p_lieu_local: Dans quel bloc se situe le local [A/B/C]
        :param p_superficie_local: La superficie du local en mètres carrés
        :param p_nombre_places: Le nombre de places du local
        :param p_liste_etudiants: La liste des étudiants dans ce local
        :param p_marque_ordinateurs: La marque des ordinateurs
        :param p_nombre_ordinateurs: Le nombre d'ordinateurs
        :param p_projecteur: S'il y a un projecteur [True/False]
        """
        Local.__init__(self, p_type_local, p_numero_local, p_lieu_local, p_superficie_local,
                       p_nombre_places, p_liste_etudiants)
        self._marque_ordinateurs = p_marque_ordinateurs
        self._nombre_ordinateurs = p_nombre_ordinateurs
        self.projecteur = p_projecteur

    @property
    def marque_ordinateurs(self):
        return self._marque_ordinateurs

    @marque_ordinateurs.setter
    def marque_ordinateurs(self, v_marque_ordinateurs):
        if isinstance(v_marque_ordinateurs, str) and len(v_marque_ordinateurs) < 100:
            self._marque_ordinateurs = v_marque_ordinateurs
        else:
            raise ValueError("La marque de l'ordinateur doit être en-dessous de 100 caractères !")

    @property
    def nombre_ordinateurs(self):
        return self._nombre_ordinateurs

    @nombre_ordinateurs.setter
    def nombre_ordinateurs(self, v_nombre_ordinateurs):
        if isinstance(v_nombre_ordinateurs, int) and 0 < v_nombre_ordinateurs < 25:
            self._nombre_ordinateurs = v_nombre_ordinateurs
        else:
            raise ValueError("Le nombre d'ordinateurs doit être en-dessous de 25 !")
