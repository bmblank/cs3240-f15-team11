from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from projectSite import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from reports.models import Report
from .forms import ReportForm, UserForm
from django.template import RequestContext, loader
from django.utils import timezone
from django.contrib.auth import models
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .forms import GivePermissionsForm



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

def checkIfUserisSM(request):
    valid_groups = request.user.groups.all()
    valid_group_names = []

    for g in valid_groups:
        valid_group_names.append(g.name)

    if 'SiteManager' in valid_group_names:
        return True
    else:
        return False

@login_required
def ReportList(request):

    userIsSiteManager = checkIfUserisSM(request)
    reports_list = Report.objects.order_by('title')
    
    has_permission_to_view_reports_list = []

    valid_groups = request.user.groups.all()
    valid_group_names = []

    for g in valid_groups:
        valid_group_names.append(g.name)

    print("THE GROUP", valid_group_names)

    for item in reports_list:
        print(item.group_name)
        if item.group_name in valid_group_names or userIsSiteManager:
            print("VALID!!")
            has_permission_to_view_reports_list.append(item)

    print("HAS PERMISSION", has_permission_to_view_reports_list)



    print(reports_list)
    template = loader.get_template('index/report.html')
    # context = {'reports_list': reports_list}
    context = {'has_permission_to_view_reports_list': has_permission_to_view_reports_list}
    return render(request, 'index/report.html', context)

@login_required
def detail(request, report_id):
    r = get_object_or_404(Report, pk=report_id)
    return render(request, 'index/detail.html', {'r': r})

def GivePermissions(request):

    valid_groups = request.user.groups.all()
    valid_group_names = []

    all_users = User.objects.all()


    for g in valid_groups:
        valid_group_names.append(g.name)

    if 'SiteManager' in valid_group_names:
        valid_groups = Group.objects.all()
        valid_group_names = []
        for g in valid_groups:
            valid_group_names.append(g.name)

    if request.method == "POST":
        permission_form = GivePermissionsForm(request.POST)

        selected_user = request.POST.get("user")
        selected_group = request.POST.get("group")

        if selected_group in valid_group_names:
            print("HOORAY, selected group is in valid_group names")
            possible_group = Group.objects.get(name=selected_group)
            possible_group.user_set.add(selected_user)

        else:
            print("This group does not exist or you do not have permission to add people to this group")



        print(request.POST.get("user"))
    else:
        permission_form = GivePermissionsForm()





    return render(request, 'index/givepermissions.html', {'permission_form': permission_form, 'valid_group_names': valid_group_names})


def Register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)

            public_group = Group.objects.get(name='Public')
            public_group.user_set.add(user)

            user.save()
            registered = True
            print("USER SUCCESS!")
        else:
            print("USER ERROR!")
    else:
        user_form = UserForm()


    # user_form = UserForm()
    return render(request, 'index/register.html', {'user_form': user_form})



@login_required
def create(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.author = request.user
            report.created = timezone.now()
            
            #if created == False, means that group already exists
            new_group, created = Group.objects.get_or_create(name=report.group_name)

            if created == True:
                new_group.user_set.add(request.user)
                report.save()
            else:
                valid_users = new_group.user_set.all()
                print("HEEY", valid_users)

                userIsSiteManager = checkIfUserisSM(request)

                if request.user not in valid_users and not userIsSiteManager:
                    print("You are not allowed to post to this group.")
                    # messages.error(request, 'Document deleted.')
                    # pass
                else:
                    report.save()

                # new_group.save()
                # current_user = request.user
                # current_user.groups.add(new_group)
                # current_user.save()

            return render(request, 'index/report.html')

    else:
        form = ReportForm
    return render(request, 'index/create.html', {'form': form})
