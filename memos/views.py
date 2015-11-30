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
from Crypto.PublicKey import RSA
from Crypto import Random





# Create your views here.

@login_required
def Inbox(request):
    inbox_list = Memo.objects.order_by('-created')
    personal_inbox = []
    for m in inbox_list:
        if m.recipient_username == request.user.username:
            personal_inbox.append(m)
    print("THIS IS THE PERSONAL INBOX", personal_inbox)





    context = {'personal_inbox': personal_inbox}
    return render(request, 'memos/inbox.html', context)


@login_required
def NewMemo(request):
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.sender =request.user
            memo.body = request.POST.get('body')
            memo.subject = request.POST.get('subject')
            memo.created = timezone.now()
            
            user_list = User.objects.all()
            user_names = []
            #public_keys = []
            for u in user_list:
                user_names.append(u.username)
                #public_keys.append(u.publicKey)


            if memo.recipient_username in user_names:
                index_val = user_names.index(memo.recipient_username)
                memo.recipient = User.objects.all()[index_val]
                print("THIS IS THE MEMO recipient", memo.recipient)

                memo.body = encryptBody(memo.body)

                memo.save()

            else:
                print("NOT A VALID USER!!!")

            return redirect('memos.views.Inbox')

    else:
        form = MemoForm
    return render(request, 'memos/newmemo.html', {'form': form})

@login_required
def MemoDetails(request, memo_id):
    r = get_object_or_404(Memo, pk=memo_id)
    return render(request, 'memos/memodetails.html', {'r': r})

def DeleteMemo(request, memo_id):
    Memo.objects.filter(id=memo_id).delete()
    return redirect('memos.views.Inbox')

randomGen = Random.new().read
key = RSA.generate(1024, randomGen)

def encryptBody(text):
    return key.publickey().encrypt(text.encode('utf-8'), 32)

def decryptBody(text):
    return key.decrypt(text)