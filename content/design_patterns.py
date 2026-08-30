"""Parcours 23 — Design Patterns & Typage Moderne."""

LEVEL = {
    "id": "design_patterns",
    "title": "23 · Design Patterns & Typage Moderne",
    "lessons": [
        {
            "id": "pat-01",
            "title": "Le pattern Factory (Fabrique)",
            "content": """## Créer des objets sans coupler les classes

Le patron de conception **Factory** (Fabrique) délègue l'instanciation des
objets à une fonction ou méthode spécialisée : le code appelant n'a pas
besoin de connaître les classes concrètes créées.

```python
class Chien:
    def parler(self): return "Ouaf"

class Chat:
    def parler(self): return "Miaou"

def fabriquer_animal(type_animal):
    if type_animal == "chien":
        return Chien()
    elif type_animal == "chat":
        return Chat()
    raise ValueError(f"Animal inconnu : {type_animal}")
```

## À toi

Écris deux classes `Voiture` (avec méthode `type()` qui renvoie `"voiture"`) et
`Moto` (avec méthode `type()` qui renvoie `"moto"`), ainsi qu'une fonction
`fabrique_vehicule(nom: str)` qui instancie et renvoie la bonne classe
selon que `nom` vaut `"voiture"` ou `"moto"` (lève `ValueError` sinon).""",
            "starter": "class Voiture:\n    def type(self) -> str:\n        ...\n\nclass Moto:\n    def type(self) -> str:\n        ...\n\ndef fabrique_vehicule(nom: str):\n    ...\n",
            "check": "v = fabrique_vehicule('voiture')\n"
                     "m = fabrique_vehicule('moto')\n"
                     "assert v.type() == 'voiture'\n"
                     "assert m.type() == 'moto'\n"
                     "try:\n"
                     "    fabrique_vehicule('fusee')\n"
                     "    assert False, 'Aurait du lever ValueError'\n"
                     "except ValueError:\n"
                     "    pass\n",
            "solution": "class Voiture:\n    def type(self) -> str:\n        return 'voiture'\n\n"
                        "class Moto:\n    def type(self) -> str:\n        return 'moto'\n\n"
                        "def fabrique_vehicule(nom: str):\n"
                        "    if nom == 'voiture':\n        return Voiture()\n"
                        "    elif nom == 'moto':\n        return Moto()\n"
                        "    raise ValueError(f'Inconnu: {nom}')\n",
            "hints": [
                "Implémente def type(self): return 'voiture' dans Voiture.",
                "Dans fabrique_vehicule, teste si nom == 'voiture' ou 'moto', sinon raise ValueError."
            ],
        },
        {
            "id": "pat-02",
            "title": "Le pattern Observateur (Event Emitter)",
            "content": """## Découpler les composants par des abonnements

Le pattern **Observateur** permet à un objet émetteur de notifier
automatiquement une liste d'abonnés (callbacks) dès qu'un événement survient,
sans avoir besoin de connaître qui écoute.

```python
class EventEmitter:
    def __init__(self):
        self._auditeurs = []

    def abonner(self, callback):
        self._auditeurs.append(callback)

    def notifier(self, *args, **kwargs):
        for cb in self._auditeurs:
            cb(*args, **kwargs)
```

## À toi

Écris la classe `GestionnaireEvenements` avec :
- `__init__(self)` : initialise la liste des abonnés.
- `abonner(self, callback)` : enregistre la fonction `callback`.
- `emettre(self, donnees)` : appelle tous les callbacks enregistrés en leur passant `donnees`.""",
            "starter": "class GestionnaireEvenements:\n    def __init__(self):\n        ...\n\n    def abonner(self, callback):\n        ...\n\n    def emettre(self, donnees):\n        ...\n",
            "check": "ge = GestionnaireEvenements()\n"
                     "reçus = []\n"
                     "ge.abonner(lambda d: reçus.append(d * 2))\n"
                     "ge.abonner(lambda d: reçus.append(d + 1))\n"
                     "ge.emettre(10)\n"
                     "assert reçus == [20, 11]\n",
            "solution": "class GestionnaireEvenements:\n"
                        "    def __init__(self):\n"
                        "        self._callbacks = []\n\n"
                        "    def abonner(self, callback):\n"
                        "        self._callbacks.append(callback)\n\n"
                        "    def emettre(self, donnees):\n"
                        "        for cb in self._callbacks:\n"
                        "            cb(donnees)\n",
            "hints": [
                "Stocke les callbacks dans une liste self._callbacks = [].",
                "Dans emettre(donnees), boucle sur chaque cb et appelle cb(donnees)."
            ],
        },
        {
            "id": "pat-03",
            "title": "Le pattern Stratégie",
            "content": """## Rendre les algorithmes interchangeables

Le patron **Stratégie** permet de changer dynamiquement la façon dont un
calcul est effectué sans modifier la classe principale.

Exemple pour des stratégies de réduction de prix :
- `SansReduction` : renvoie le prix brut `prix`.
- `PourcentageReduction(20)` : applique 20% de remise (`prix * 0.8`).
- `MontantFixeReduction(15)` : soustrait 15€ (`max(0, prix - 15)`).

## À toi

Écris la classe `CalculateurPrix` qui prend une stratégie lors de son
instanciation `CalculateurPrix(strategie)` et possède une méthode
`calculer(prix_base: float) -> float` qui applique la stratégie passée
(la stratégie étant un objet ou une fonction qui prend `prix_base` en argument).""",
            "starter": "class CalculateurPrix:\n    def __init__(self, strategie):\n        ...\n\n    def calculer(self, prix_base: float) -> float:\n        ...\n",
            "check": "strat_20 = lambda p: p * 0.8\n"
                     "strat_fixe = lambda p: max(0.0, p - 10.0)\n"
                     "c1 = CalculateurPrix(strat_20)\n"
                     "c2 = CalculateurPrix(strat_fixe)\n"
                     "assert c1.calculer(100.0) == 80.0\n"
                     "assert c2.calculer(100.0) == 90.0\n",
            "solution": "class CalculateurPrix:\n"
                        "    def __init__(self, strategie):\n"
                        "        self.strategie = strategie\n\n"
                        "    def calculer(self, prix_base: float) -> float:\n"
                        "        return self.strategie(prix_base)\n",
            "hints": [
                "Enregistre self.strategie = strategie dans __init__.",
                "Dans calculer, renvoie self.strategie(prix_base)."
            ],
        },
        {
            "id": "pat-04",
            "title": "Classes abstraites & Interfaces (abc.ABC)",
            "content": """## Imposer un contrat avec abc.ABC

Pour forcer les classes dérivées à implémenter certaines méthodes obligatoires,
Python fournit le module `abc` (Abstract Base Classes) et le décorateur
`@abstractmethod` :

```python
from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def aire(self) -> float:
        pass

# Impossible d'instancier Forme() directement !
# Toute sous-classe qui n'implémente pas aire() lèvera TypeError.
```

## À toi

Définis une classe abstraite `Notificateur(ABC)` avec une méthode abstraite
`@abstractmethod def envoyer(self, message: str) -> str: pass`, puis crée
une classe concrète `NotificateurEmail(Notificateur)` qui implémente
`envoyer(self, message)` et renvoie `f"[EMAIL] {message}"`.""",
            "starter": "from abc import ABC, abstractmethod\n\nclass Notificateur(ABC):\n    ...\n\nclass NotificateurEmail(Notificateur):\n    ...\n",
            "check": "from abc import ABC\n"
                     "assert issubclass(Notificateur, ABC)\n"
                     "try:\n"
                     "    Notificateur()\n"
                     "    assert False, 'Notificateur ne doit pas etre instanciable'\n"
                     "except TypeError:\n"
                     "    pass\n"
                     "ne = NotificateurEmail()\n"
                     "assert ne.envoyer('Bonjour') == '[EMAIL] Bonjour'\n",
            "solution": "from abc import ABC, abstractmethod\n\n"
                        "class Notificateur(ABC):\n"
                        "    @abstractmethod\n"
                        "    def envoyer(self, message: str) -> str:\n"
                        "        pass\n\n"
                        "class NotificateurEmail(Notificateur):\n"
                        "    def envoyer(self, message: str) -> str:\n"
                        "        return f'[EMAIL] {message}'\n",
            "hints": [
                "Décore la méthode avec @abstractmethod.",
                "Dans NotificateurEmail, implémente def envoyer(self, message): return f'[EMAIL] {message}'."
            ],
        },
        {
            "id": "pat-05",
            "title": "Typage structurel avec Protocol (Duck Typing)",
            "content": """## Typage statique moderne avec typing.Protocol

Le typage nominal classique exige d'hériter explicitement d'une classe de base.
Avec `typing.Protocol` (introduit dans Python 3.8 / PEP 544), on définit une
interface par sa **structure** : tout objet qui possède les méthodes requises
est automatiquement compatible sans héritage forcé !

```python
from typing import Protocol

class Dessinable(Protocol):
    def dessiner(self) -> None:
        ...

# N'importe quelle classe avec def dessiner(self): ... est considérée comme un Dessinable !
```

## À toi

Définis un protocole `Sauvegardable(Protocol)` avec une méthode `sauvegarder(self) -> bool: ...`
et une fonction `sauvegarder_tous(elements: list)` qui appelle `.sauvegarder()`
sur chaque élément de la liste et renvoie `True` si tous ont renvoyé `True`, sinon `False`.""",
            "starter": "from typing import Protocol\n\nclass Sauvegardable(Protocol):\n    def sauvegarder(self) -> bool:\n        ...\n\ndef sauvegarder_tous(elements: list) -> bool:\n    ...\n",
            "check": "class Document:\n"
                     "    def sauvegarder(self): return True\n"
                     "class Image:\n"
                     "    def sauvegarder(self): return False\n"
                     "assert sauvegarder_tous([Document(), Document()]) is True\n"
                     "assert sauvegarder_tous([Document(), Image()]) is False\n"
                     "assert sauvegarder_tous([]) is True\n",
            "solution": "from typing import Protocol\n\n"
                        "class Sauvegardable(Protocol):\n"
                        "    def sauvegarder(self) -> bool:\n"
                        "        ...\n\n"
                        "def sauvegarder_tous(elements: list) -> bool:\n"
                        "    return all(e.sauvegarder() for e in elements)\n",
            "hints": [
                "Utilise la fonction standard all(e.sauvegarder() for e in elements).",
                "Renvoie True pour une liste vide."
            ],
        },
        {
            "id": "pat-06",
            "title": "Énumérations robustes avec Enum",
            "content": """## Remplacer les chaînes magiques par enum.Enum

Utiliser des chaînes de caractères brutes (comme `"en_cours"`, `"termine"`, `"annule"`)
expose votre code aux fautes de frappe silencieuses.

Le module standard `enum` permet de définir des constantes nommées sûres :

```python
from enum import Enum, auto

class Statut(Enum):
    BROUILLON = auto()
    PUBLIE = auto()
    ARCHIVE = auto()

etat = Statut.PUBLIE
if etat == Statut.PUBLIE:
    print("Article en ligne !")
```

## À toi

Crée une énumération `NiveauAlerte(Enum)` avec trois membres :
- `INFO = 1`
- `ATTENTION = 2`
- `CRITIQUE = 3`

Puis écris `est_urgent(niveau: NiveauAlerte) -> bool` qui renvoie `True` si
le niveau est `NiveauAlerte.CRITIQUE`, sinon `False`.""",
            "starter": "from enum import Enum\n\nclass NiveauAlerte(Enum):\n    ...\n\ndef est_urgent(niveau: NiveauAlerte) -> bool:\n    ...\n",
            "check": "assert NiveauAlerte.INFO.value == 1\n"
                     "assert NiveauAlerte.CRITIQUE.value == 3\n"
                     "assert est_urgent(NiveauAlerte.CRITIQUE) is True\n"
                     "assert est_urgent(NiveauAlerte.ATTENTION) is False\n"
                     "assert est_urgent(NiveauAlerte.INFO) is False\n",
            "solution": "from enum import Enum\n\n"
                        "class NiveauAlerte(Enum):\n"
                        "    INFO = 1\n"
                        "    ATTENTION = 2\n"
                        "    CRITIQUE = 3\n\n"
                        "def est_urgent(niveau: NiveauAlerte) -> bool:\n"
                        "    return niveau == NiveauAlerte.CRITIQUE\n",
            "hints": [
                "Déclare INFO = 1, ATTENTION = 2, CRITIQUE = 3 dans la classe NiveauAlerte(Enum).",
                "Renvoie niveau == NiveauAlerte.CRITIQUE."
            ],
        },
        {
            "id": "qz-pat",
            "type": "quiz",
            "title": "Quiz — Design Patterns & Typage",
            "question": "Quelle est la différence fondamentale entre `abc.ABC` (classes abstraites) et `typing.Protocol` en Python ?",
            "options": [
                "Protocol est plus lent à l'exécution que ABC.",
                "ABC impose un héritage nominal explicite, tandis que Protocol permet le Duck Typing structurel sans sous-classement forcé.",
                "ABC ne fonctionne qu'avec des fonctions et pas des classes.",
                "Protocol ne supporte pas les annotations de type."
            ],
            "answer": 1,
            "explanation": "ABC vérifie l'héritage formel au moment de l'instanciation (__subclasscheck__), alors que typing.Protocol vérifie que la structure (méthodes et attributs) correspond au contrat, ce qui correspond au Duck Typing statique."
        }
    ]
}
