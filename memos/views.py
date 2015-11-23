from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from projectSite import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Memo
from .forms import MemoForm
from django.template import RequestContext, loader
from django.utils import timezone
from django.contrib.auth import models
from django.contrib.auth.models import User, Group
from django.contrib import messages




# Create your views here.

@login_required
def Inbox(request):
    inbox_list = Memo.objects.order_by('subject')

    context = {'inbox_list': inbox_list}
    return render(request, 'memos/inbox.html', context)


@login_required
def NewMemo(request):
    if request.method == "POST":
        form = MemoForm(request.POST)
        sender = request.user
        if form.is_valid():
            memo = form.save(commit=False, sender=request.user)
            memo.save()
            return render(request, 'index/memos.html')

    else:
        form = MemoForm
    return render(request, 'memos/newmemo.html', {'form': form})

@login_required
def MemoDetails(request, memo_id):
    r = get_object_or_404(Memo, pk=memo_id)
    return render(request, 'memos/memodetails.html', {'r': r})