from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('user_reservations', user_id=request.user.id)
    else:
        form = ReservationForm()
    return render(request, 'reservations/form.html', {'form': form})

def reservation_detail(request, id):
    reservation = Reservation.objects.get(id=id)
    return render(request, 'reservations/detail.html', {'reservation': reservation})

def user_reservations(request, user_id):
    reservations = Reservation.objects.filter(user_id=user_id)
    return render(request, 'reservations/list.html', {'reservations': reservations})
