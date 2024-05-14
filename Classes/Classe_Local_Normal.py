from Classes.Classe_Local import Local
from Classes.Classe_Etudiant import Etudiant

class Local_Normal(Local):

    def __init__(self, p_type_local: str = "", p_numero_local: str = "", p_lieu_local: str = "",
                 p_superficie_local: float = 0.0, p_nombre_places: int = 0, p_liste_etudiants: list[Etudiant] = None,
                 p_nombre_places_par_table: int = 0):
        """
        Constructeur de la classe Local_Normal
        :param p_type_local: Le type de local
        :param p_numero_local: Le numéro du local
        :param p_lieu_local: Dans quel bloc se situe le local [A/B/C]
        :param p_superficie_local: La superficie du local en mètres carrés
        :param p_nombre_places: Le nombre de places du local
        :param p_liste_etudiants: La liste des étudiants dans ce local
        :param p_nombre_places_par_table: Le nombre de places par table
        """
        Local.__init__(self, p_type_local, p_numero_local, p_lieu_local, p_superficie_local, p_nombre_places, p_liste_etudiants)
        self._nombre_places_par_table = p_nombre_places_par_table

    @property
    def nombre_places_par_table(self):
        return self._nombre_places_par_table

    @nombre_places_par_table.setter
    def nombre_places_par_table(self, v_nombre_places_par_table):
        if isinstance(v_nombre_places_par_table, int) and (v_nombre_places_par_table == 1 or v_nombre_places_par_table == 2):
            self._nombre_places_par_table = v_nombre_places_par_table
        else:
            raise ValueError("Le nombre de places par table peut seulement être 1 ou 2 !")

