from django.shortcuts import render
from django.http import JsonResponse

from .models import Summary
from .models import (
    Duxu1000009,
    Hanhui1000002,
    Haowei1000008,
    Likun1000003,
    Panxian1000005,
    Shenxian1000004,
    Xiexiao1000001,
    Xiezhi1000006,
    Zengpeng1000000,
    Zouan1000007,
)

from django.db.models import Sum


def index(request):
    return render(request, 'index.html')


def summary_page(request):
    summary_df = Summary.objects.values("driverID", "carPlateNumber").annotate(
        total_number_of_overspeed=Sum('number_of_overspeed'),
        total_overspeed=Sum('total_overspeed'),
        total_number_of_fatigue_driving=Sum('number_of_fatigueDriving'),
        total_neutral_slide=Sum('number_of_neutralSlide'),
        total_neutral_slide_time=Sum('total_neutralSlideTime')
    ).order_by("driverID")

    summary = summary_df.values_list(
        "driverID",
        "carPlateNumber",
        "total_number_of_overspeed",
        "total_overspeed",
        "total_number_of_fatigue_driving",
        "total_neutral_slide",
        "total_neutral_slide_time"
    )

    return render(request, 'summary_report.html', {'summary': summary})


def choose_page(request):
    drivers = Summary.objects.values('driverID', 'carPlateNumber').distinct().order_by("driverID")
    context = {'driver_list': drivers}
    return render(request, 'driver.html', context)


def monitor_data(request):
    driverID = request.GET.get("driverID")
    time = int(request.GET.get("time"))

    if driverID == "duxu1000009":
        model = Duxu1000009.objects
    elif driverID == "hanhui1000002":
        model = Hanhui1000002.objects
    elif driverID == "haowei1000008":
        model = Haowei1000008.objects
    elif driverID == "likun1000003":
        model = Likun1000003.objects
    elif driverID == "panxian1000005":
        model = Panxian1000005.objects
    elif driverID == "shenxian1000004":
        model = Shenxian1000004.objects
    elif driverID == "xiexiao1000001":
        model = Xiexiao1000001.objects
    elif driverID == "xiezhi1000006":
        model = Xiezhi1000006.objects
    elif driverID == "zengpeng1000000":
        model = Zengpeng1000000.objects
    elif driverID == "zouan1000007":
        model = Zouan1000007.objects

    related_data = model.filter(unix_Time__gte=(time - 30), unix_Time__lte=time).order_by('unix_Time').values(
        'unix_Time', 'speed', 'isOverspeed')

    return_payload = {
        "driverID": driverID,
        "time": time,
        "speed": list(related_data.values())
    }

    return JsonResponse(return_payload)


def monitor_page(request, driverID):
    return render(request, 'monitor.html', {'driverID': driverID})
