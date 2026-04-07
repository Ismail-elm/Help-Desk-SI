# tickets/models.py
from django.db import models

class Ticket(models.Model):
    PRIORITE_CHOICES = [
        ('basse', 'Basse'),
        ('moyenne', 'Moyenne'),
        ('haute', 'Haute'),
        ('critique', 'Critique'),
    ]
    STATUT_CHOICES = [
        ('ouvert', 'Ouvert'),
        ('en_cours', 'En cours'),
        ('resolu', 'Résolu'),
    ]
    MODULE_CHOICES = [
        ('MM', 'MM – Achats'),
        ('SD', 'SD – Ventes'),
        ('FI', 'FI – Finance'),
        ('PP', 'PP – Production'),
        ('WM', 'WM – Entrepôt'),
        ('QM', 'QM – Qualité'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()
    module_sap = models.CharField(max_length=10, choices=MODULE_CHOICES)
    priorite = models.CharField(max_length=10, choices=PRIORITE_CHOICES, default='moyenne')
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='ouvert')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.module_sap}] {self.titre} — {self.statut}"