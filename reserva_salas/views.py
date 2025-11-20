from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import SalaEstudio, Reserva
from .forms import ReservaForm

# Create your views here.
def lista_salas(request):
    salas = SalaEstudio.objects.all().order_by('nombre')

    for sala in salas:
        if not sala.disponible:
            ultima_reserva = Reserva.objects.filter(sala_reservada=sala).last()
            if ultima_reserva:
                if timezone.now() > ultima_reserva.hora_termino:
                    sala.disponible = True
                    sala.save()
    return render(request, 'reserva_salas/lista_salas.html', {'salas':salas})

def detalle_reserva(request, sala_id):
    sala = get_object_or_404(SalaEstudio, pk=sala_id)

    reserva_activa = None

    if not sala.disponible:
        reserva_activa = Reserva.objects.filter(sala_reservada=sala).last()

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.sala_reservada = sala

            ahora = timezone.now()
            reserva.hora_inicio = ahora
            reserva.hora_termino = ahora + timedelta(hours=2)

            reserva.save()

            sala.disponible = False
            sala.save()
            
            return redirect('lista_salas')
    else:
        form = ReservaForm()

    return render(request, 'reserva_salas/detalle_sala.html', {'sala':sala, 'form':form, 'reserva_activa':reserva_activa})