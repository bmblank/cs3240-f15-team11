from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from projectSite import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from reports.models import Report
from django.template import RequestContext, loader

def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "index/login.html", {'redirect_to': next})

def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

@login_required
def Home(request):
    return render(request, "index/home.html", {})

@login_required
def ReportList(request):
    reports_list = Report.objects.order_by('title')[:5]
    print(reports_list)
    template = loader.get_template('index/report.html')
    context = {'reports_list': reports_list}
    return render(request, 'index/report.html', context)

@login_required
def detail(request, report_id):
    r = get_object_or_404(Report, pk=report_id)
    return render(request, 'index/detail.html', {'r': r})