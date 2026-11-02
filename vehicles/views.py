

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle
from .forms import VehicleForm


# Landing Page
def home(request):
    return render(request, 'home.html')


# Add Vehicle
def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()

    return render(request, 'add.html', {'form': form})


# Display All Vehicles
def vehicle_list(request):
    vehicles = Vehicle.objects.all()

    return render(request, 'list.html',
                  {'vehicles': vehicles})


# Vehicle Details
def vehicle_detail(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)

    return render(request, 'detail.html',
                  {'vehicle': vehicle})


# Update Vehicle
def update_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)

    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)

        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)

    return render(request, 'update.html',
                  {'form': form})


# Delete Vehicle
def delete_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)

    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')

    return render(request, 'delete.html',
                  {'vehicle': vehicle})