from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from .forms import EquipmentForm
from .models import Printer, HandDryer, FluorescentTube, Floodlight, Amplifier, Photocopier, Computers
from django.contrib import messages


def IndexView(request):
    return render(request, "home/main2.html")


def CostcalView(request):
    # if this is a POST request process the form data
    global form
    if request.method == 'POST':
        val_1 = request.POST['equipment_name']
        val_2 = request.POST['quantity']
        val_3 = request.POST['rating']
        val_4 = request.POST['hours_used']

        if val_1 == 'Printers':
            cost = int(val_4) * int(val_3) * 10 * int(val_2)
            ins = Printer(hours_used=val_4, daily_cost=cost)
            ins.save()

        elif val_1 == 'HandDryer':
            cost = int(val_4) * int(val_3) * 10 * int(val_2)
            ins = HandDryer(hours_used=val_4, daily_cost=cost)
            ins.save()

        elif val_1 == 'FluorescentTube':
            cost = int(val_4) * int(val_3) * 10 * int(val_2)
            ins = FluorescentTube(hours_used=val_4, daily_cost=cost)
            ins.save()

        elif val_1 == 'Floodlights':
            cost = int(val_4) * int(val_3) * 10 * int(val_2)
            ins = Floodlight(hours_used=val_4, daily_cost=cost)
            ins.save()

        elif val_1 == 'Amplifiers':
            cost = int(val_4) * int(val_3) * 10 * int(val_2)
            ins = Amplifier(hours_used=val_4, daily_cost=cost)
            ins.save()

        elif val_1 == 'Computers':
            cost = int(val_4) * int(val_3) * 10 * int(val_2)
            ins = Computers(hours_used=val_4, daily_cost=cost)
            ins.save()

        elif val_1 == 'Photocopier':
            cost = int(val_4) * int(val_3) * 10 * int(val_2)
            ins = Photocopier(hours_used=val_4, daily_cost=cost)
            ins.save()

        else:
            messages.success(request, 'error')


        # redirect to a new URL:
        #return HttpResponse('thanks')
        messages.success(request, 'Equipment added successfully, to add another, click add equipment...')

    # if a GET (or any other method) create a blank form
    else:
        form = EquipmentForm()
    return render(request, 'home/costcal.html', {'form': form})





