from django.shortcuts import render
from django.http import JsonResponse

from .models import Summary
from .models import DriveData

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

    context = {
        'summary': summary,
    }
    return render(request, 'summary_report.html', context)


def choose_page(request):
    drivers = Summary.objects.values('driverID', 'carPlateNumber').distinct().order_by("driverID")
    context = {'driver_list': drivers}
    return render(request, 'driver.html', context)


def graph_page(request):
    summary = Summary.objects.values("driverID").annotate(
        total_number_of_overspeed=Sum('number_of_overspeed'),
        total_overspeed=Sum('total_overspeed'),
        total_number_of_fatigue_driving=Sum('number_of_fatigueDriving'),
        total_neutral_slide=Sum('number_of_neutralSlide'),
        total_neutral_slide_time=Sum('total_neutralSlideTime')
    ).order_by("driverID")
    ids = []
    overspeed = []
    overspeed_time = []
    fatigue_driving = []
    neutral_slide = []
    neutral_slide_time = []
    for i in summary:
        driver = dict(i)
        print(driver)
        ids.append(driver["driverID"])
        overspeed.append(driver['total_number_of_overspeed'])
        overspeed_time.append(driver['total_overspeed'])
        fatigue_driving.append(driver['total_number_of_fatigue_driving'])
        neutral_slide.append(driver['total_neutral_slide'])
        neutral_slide_time.append(driver['total_neutral_slide_time'])
    names = ['Total Times of Overspeed', 'Total Duration of Overspeed', 'Total Times of Fatigue Driving',
             'Total Times of Neutral Slide', 'Total Duration of Neutral Slide']
    sums = [overspeed, overspeed_time, fatigue_driving, neutral_slide, neutral_slide_time]
    print(sums)
    return render(request, 'chart.html', {"sum": sums, "drivers": ids, "names": names})


def monitor_data(request):
    driverID = request.GET.get("driverID")
    time = int(request.GET.get("time"))

    related_data = DriveData.objects.filter(unix_Time__gte=(time - 30), unix_Time__lte=time,
                                            driverID=driverID).order_by('unix_Time').values(
        'unix_Time', 'speed', 'isOverspeed')

    return_payload = {
        "driverID": driverID,
        "time": time,
        "speed": list(related_data.values())
    }

    return JsonResponse(return_payload)


def monitor_page(request, driverID):
    return render(request, 'monitor.html', {'driverID': driverID})
