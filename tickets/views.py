# tickets/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Ticket
from .forms import TicketForm

def liste_tickets(request):
    tickets = Ticket.objects.all().order_by('-date_creation')
    stats = {
        'total': tickets.count(),
        'ouverts': tickets.filter(statut='ouvert').count(),
        'en_cours': tickets.filter(statut='en_cours').count(),
        'resolus': tickets.filter(statut='resolu').count(),
        'critiques': tickets.filter(priorite='critique').count(),
    }
    stats_display = [
        ('Total', stats['total'], 'stat-total'),
        ('Ouverts', stats['ouverts'], 'stat-ouverts'),
        ('En cours', stats['en_cours'], 'stat-en-cours'),
        ('Résolus', stats['resolus'], 'stat-resolus'),
        ('Critiques', stats['critiques'], 'stat-critiques'),
    ]
    return render(request, 'tickets/liste.html', {'tickets': tickets, 'stats_display': stats_display})

def creer_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_tickets')
    else:
        form = TicketForm()
    return render(request, 'tickets/form.html', {'form': form, 'action': 'Créer'})

def detail_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'tickets/detail.html', {'ticket': ticket})

def modifier_statut(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        nouveau_statut = request.POST.get('statut')
        if nouveau_statut in dict(Ticket.STATUT_CHOICES):
            ticket.statut = nouveau_statut
            ticket.save()
    return redirect('detail_ticket', pk=pk)

def export_json(request):
    tickets = Ticket.objects.all().values(
        'id', 'titre', 'module_sap', 'priorite', 'statut',
        'date_creation', 'date_modification'
    )
    return JsonResponse(list(tickets), safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})