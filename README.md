# 🖥️ Help Desk SI – Système de gestion de tickets de support

Application web de gestion de tickets de support informatique, inspirée des flux de traitement d'anomalies SAP.
Développée en Python/Django.

## ✨ Fonctionnalités

- 🗂️ Création et suivi de tickets d'anomalie par module SAP (MM, SD, FI, PP, WM, QM)
- 🚨 Gestion des priorités (Basse / Moyenne / Haute / Critique)
- 🔄 Cycle de vie des tickets : Ouvert → En cours → Résolu
- 📊 Tableau de bord avec statistiques en temps réel
- 📤 Export des tickets au format JSON

## 🛠️ Stack technique

- 🐍 **Backend** : Python 3, Django
- 🗄️ **Base de données** : SQLite
- 🎨 **Frontend** : HTML/CSS natif

## ⚙️ Installation

```bash
git clone https://github.com/Ismail-elm/Help-Desk-SI.git
cd Help-Desk-SI
python -m venv venv
source venv/bin/activate  # Windows : venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

▶️ Accès : http://127.0.0.1:8000/tickets/

## 📌 Contexte

Projet réalisé pour illustrer une compréhension concrète
des problématiques de support SAP (gestion d'anomalies, suivi de correctifs, reporting).
