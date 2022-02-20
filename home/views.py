from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from .forms import EquipmentForm, MeterReadingForm
from .models import Printer, HandDryer, FluorescentTube, Floodlight, Amplifier, Photocopier, Computers, MeterReading, \
    Meter1, Meter2, Meter3, HistoryData
from django.contrib import messages

import pandas as ps
import plotly.express as px
from plotly.offline import plot
from django.views.generic.base import TemplateView

import numpy
from numpy import mean


def IndexView(request):
    return render(request, "home/main2.html")


def CostcalView(request):
    # if this is a POST request process the form data
    global form
    price = 10.00
    form = EquipmentForm()
    if request.method == 'POST':
        val_1 = request.POST['equipment_name']
        val_2 = request.POST['quantity']
        val_3 = request.POST['rating']
        val_4 = request.POST['hours_used']

        if val_1 == 'Printers':
            cost = float(val_4) * float(val_3) * price * float(val_2)
            cons = float(val_4) * float(val_3) * float(val_2)
            ins = Printer(hours_used=val_4, daily_cost=cost, consumption=cons)
            ins.save()

        elif val_1 == 'HandDryer':
            cost = float(val_4) * float(val_3) * price * float(val_2)
            cons = float(val_4) * float(val_3) * float(val_2)
            ins = HandDryer(hours_used=val_4, daily_cost=cost, consumption=cons)
            ins.save()

        elif val_1 == 'FluorescentTube':
            cost = float(val_4) * float(val_3) * price * float(val_2)
            cons = float(val_4) * float(val_3) * float(val_2)
            ins = FluorescentTube(hours_used=val_4, daily_cost=cost, consumption=cons)
            ins.save()


        elif val_1 == 'Floodlights':
            cost = float(val_4) * float(val_3) * price * float(val_2)
            cons = float(val_4) * float(val_3) * float(val_2)
            ins = Floodlight(hours_used=val_4, daily_cost=cost, consumption=cons)
            ins.save()

        elif val_1 == 'Amplifiers':
            cost = float(val_4) * float(val_3) * price * float(val_2)
            cons = float(val_4) * float(val_3) * float(val_2)
            ins = Amplifier(hours_used=val_4, daily_cost=cost, consumption=cons)
            ins.save()

        elif val_1 == 'Computers':
            cost = float(val_4) * float(val_3) * price * float(val_2)
            cons = float(val_4) * float(val_3) * float(val_2)
            ins = Computers(hours_used=val_4, daily_cost=cost, consumption=cons)
            ins.save()

        elif val_1 == 'Photocopier':
            cost = float(val_4) * float(val_3) * price * float(val_2)
            cons = float(val_4) * float(val_3) * float(val_2)
            ins = Photocopier(hours_used=val_4, daily_cost=cost, consumption=cons)
            ins.save()

        else:
            messages.success(request, 'error')

        # redirect to a new URL:
        # return HttpResponse('thanks')
        messages.success(request, 'Equipment added successfully, to add another, click add equipment...')

    # if a GET (or any other method) create a blank form
    else:
        form = EquipmentForm()
    return render(request, 'home/costcal.html', {'form': form})


def MeterReadingView(request):
    if request.method == "POST":
        date = request.POST['date']
        meter_id = request.POST['meter_id']
        meter_location = request.POST['meter_location']
        reading = request.POST['reading']

        if meter_id == 'Meter1':
            last_entry = Meter1.objects.values_list('reading', flat=True).last()

            # calculate consumption
            cons = float(reading) - float(last_entry)

            ins = Meter1(date=date, meter_location=meter_location, reading=reading, consumption=cons)
            ins.save()

        elif meter_id == 'Meter2':
            last_entry = Meter2.objects.values_list('reading', flat=True).last()

            # calculate consumption
            cons = float(reading) - float(last_entry)

            ins = Meter2(date=date, meter_location=meter_location, reading=reading, consumption=cons)
            ins.save()

        elif meter_id == 'Meter3':
            last_entry = Meter3.objects.values_list('reading', flat=True).last()

            # calculate consumption
            cons = float(reading) - float(last_entry)

            ins = Meter3(date=date, meter_location=meter_location, reading=reading, consumption=cons)
            ins.save()

        form = MeterReadingForm()
        messages.success(request, 'Data has been submitted')

    else:
        form = MeterReadingForm()
    return render(request, 'home/meter.html', {'form': form})


def ConsumptionView(request):
    meter1_consumption = Meter1.objects.all()
    meter2_consumption = Meter2.objects.all()
    meter3_consumption = Meter3.objects.all()

    total_consumption1 = Meter1.objects.values_list('consumption', flat=True)
    total1 = sum(total_consumption1)

    total_consumption2 = Meter2.objects.values_list('consumption', flat=True)
    total2 = sum(total_consumption2)

    total_consumption3 = Meter3.objects.values_list('consumption', flat=True)
    total3 = sum(total_consumption3)

    return render(request, 'home/consumption.html', {'meter1_consumption': meter1_consumption,
                                                     'meter2_consumption': meter2_consumption,
                                                     'meter3_consumption': meter3_consumption,
                                                     'total1': total1,
                                                     'total2': total2,
                                                     'total3': total3})


class JanuaryView(TemplateView):
    template_name = 'january.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['Week1', 'Week2', 'Week3', 'Week4']
        y = Meter3.objects.filter(date__istartswith='2022-01').values_list('consumption', flat=True)
        print(y)

        fig = px.bar(x=x, y=y,
                      labels={
                          "x": "Weeks",
                          "y": "Consumption (kWh)",
                      })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


class FebruaryView(TemplateView):
    template_name = 'february.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['Week1', 'Week2', 'Week3', 'Week4']
        y = Meter3.objects.filter(date__istartswith='2022-01').values_list('consumption', flat=True)

        fig = px.bar(x=x, y=y,
                      labels={
                          "x": "Weeks",
                          "y": "Consumption (kWh)",
                      })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


class MarchView(TemplateView):
    template_name = 'march.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['Week1', 'Week2', 'Week3', 'Week4']
        y = Meter3.objects.filter(date__istartswith='2022-01').values_list('consumption', flat=True)

        fig = px.bar(x=x, y=y,
                      labels={
                          "x": "Weeks",
                          "y": "Consumption (kWh)",
                      })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


class AprilView(TemplateView):
    template_name = 'april.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['Week1', 'Week2', 'Week3', 'Week4']
        y = Meter3.objects.filter(date__istartswith='2022-01').values_list('consumption', flat=True)

        fig = px.bar(x=x, y=y,
                      labels={
                          "x": "Weeks",
                          "y": "Consumption (kWh)",
                      })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


class MayView(TemplateView):
    template_name = 'may.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['Week1', 'Week2', 'Week3', 'Week4']
        y = Meter3.objects.filter(date__istartswith='2022-01').values_list('consumption', flat=True)

        fig = px.bar(x=x, y=y,
                      labels={
                          "x": "Weeks",
                          "y": "Consumption (kWh)",
                      })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


class JuneView(TemplateView):
    template_name = 'june.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['Week1', 'Week2', 'Week3', 'Week4']
        y = Meter3.objects.filter(date__istartswith='2022-01').values_list('consumption', flat=True)

        fig = px.bar(x=x, y=y,
                      labels={
                          "x": "Weeks",
                          "y": "Consumption (kWh)",
                      })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


class JulyView(TemplateView):
    template_name = 'july.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['Week1', 'Week2', 'Week3', 'Week4']
        y = Meter3.objects.filter(date__istartswith='2022-01').values_list('consumption', flat=True)

        fig = px.bar(x=x, y=y,
                      labels={
                          "x": "Weeks",
                          "y": "Consumption (kWh)",
                      })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


class AugustView(TemplateView):
    template_name = 'august.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['Week1', 'Week2', 'Week3', 'Week4']
        y = Meter3.objects.filter(date__istartswith='2022-01').values_list('consumption', flat=True)

        fig = px.bar(x=x, y=y,
                      labels={
                          "x": "Weeks",
                          "y": "Consumption (kWh)",
                      })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


class SeptemberView(TemplateView):
    template_name = 'september.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['Week1', 'Week2', 'Week3', 'Week4']
        y = Meter3.objects.filter(date__istartswith='2022-01').values_list('consumption', flat=True)

        fig = px.bar(x=x, y=y,
                      labels={
                          "x": "Weeks",
                          "y": "Consumption (kWh)",
                      })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


class OctoberView(TemplateView):
    template_name = 'october.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['Week1', 'Week2', 'Week3', 'Week4']
        y = Meter3.objects.filter(date__istartswith='2022-01').values_list('consumption', flat=True)

        fig = px.bar(x=x, y=y,
                      labels={
                          "x": "Weeks",
                          "y": "Consumption (kWh)",
                      })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


class NovemberView(TemplateView):
    template_name = 'november.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['Week1', 'Week2', 'Week3', 'Week4']
        y = Meter3.objects.filter(date__istartswith='2022-01').values_list('consumption', flat=True)

        fig = px.bar(x=x, y=y,
                      labels={
                          "x": "Weeks",
                          "y": "Consumption (kWh)",
                      })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


class DecemberView(TemplateView):
    template_name = 'december.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['Week1', 'Week2', 'Week3', 'Week4']
        y = Meter3.objects.filter(date__istartswith='2022-01').values_list('consumption', flat=True)

        fig = px.bar(x=x, y=y,
                      labels={
                          "x": "Weeks",
                          "y": "Consumption (kWh)",
                      })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


class DailyView(TemplateView):
    template_name = 'daily.html'

    def get_context_data(self, **kwargs):
        fluorescent_cons = FluorescentTube.objects.values_list('consumption', flat=True).last()
        floodlight_cons = Floodlight.objects.values_list('consumption', flat=True).last()
        amplifier_cons = Amplifier.objects.values_list('consumption', flat=True).last()
        printer_cons = Printer.objects.values_list('consumption', flat=True).last()

        context = super().get_context_data(**kwargs)
        x = ['Fluorescent-Tubes', 'Floodlights', 'Amplifiers', 'Printers']
        y = [fluorescent_cons, floodlight_cons, amplifier_cons, printer_cons]

        avg_consumption = mean(y)
        max_consumption = numpy.amax(y)

        equipment_value = {"Fluorescent-Tubes": fluorescent_cons,
                           "Floodlights": floodlight_cons,
                           "Amplifiers": amplifier_cons,
                           "Printers": printer_cons}
        for equipment, cons in equipment_value.items():
            if cons == max_consumption:
                print(equipment)
        for equipment_values in equipment_value.values():
            print(equipment_values)



        fig = px.line(x=x, y=y,
                      labels={
                          "x": "Equipment",
                          "y": "Consumption (kWh)",
                      })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


class AnnualView(TemplateView):
    template_name = 'annual.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',
                                                                                                                'december']
        y = HistoryData.objects.values_list('year_2017', flat=True)

        fig = px.bar(x=x, y=y,
                      labels={
                          "x": "Months",
                          "y": "Consumption (kWh)",
                      })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


class Year2018View(TemplateView):
    template_name = 'year2018.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',
             'december']
        y = HistoryData.objects.values_list('year_2018', flat=True)

        fig = px.bar(x=x, y=y,
                     labels={
                         "x": "Months",
                         "y": "Consumption (kWh)",
                     })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


class Year2021View(TemplateView):
    template_name = 'year2021.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',
             'december']
        y = HistoryData.objects.values_list('year_2021', flat=True)

        fig = px.bar(x=x, y=y,
                     labels={
                         "x": "Months",
                         "y": "Consumption (kWh)",
                     })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context
