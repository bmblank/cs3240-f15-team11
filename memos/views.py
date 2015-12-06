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
from .models import Key
from .forms import DecryptForm


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
            #memo.encrypted = request.POST.get('encrypted')

            if (request.POST.get('encrypted') == None):
                memo.encrypted = False
            else:
                memo.encrypted = True
            
            user_list = User.objects.all()
            user_names = []
            #public_keys = []
            for u in user_list:
                user_names.append(u.username)
                #public_keys.append(u.publicKey)


            if memo.recipient_username in user_names:

                recUserObj = User.objects.get(username=memo.recipient_username)
                key = Key.objects.get(user=recUserObj)

                    #key_we_need = Key.rKey.objects.all()[index_val]

                #randomG = Random.new().read
                #recipKey = RSA.generate(1024, randomG)
                #memo.body = encryptBody(memo.body, recipKey)
                #memo.body = decryptBody(memo.body, recipKey)

                print("THIS IS THE ENCRYPT CHECKBOX VAL: ", request.POST.get('encrypted'))
                if (memo.encrypted == True):
                    #memo.body = encryptBody(memo.body)

                    print("HIT THE IF STATEMENT")

                    memo.body = encryptBody(memo.body, key.publicKey)
                    #memo.body = decryptBody(memo.body, recipKey)


                else:
                    print("False was checked")

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
    if request.method == "POST":
        form = DecryptForm(request.POST)
        print("REQUEST: " + request.POST.get('decryptField'))

        #recUserObj = User.objects.get(username=memo.recipient_username)
        key = Key.objects.get(user=request.user)
        r.body = decryptBody(r.body, key.privateKey)
        #r.body = decryptBody(r.body, request.POST.get('decryptField'))
    else:
        form = DecryptForm()
    return render(request, 'memos/memodetails.html', {'r': r, 'form': form})

def DeleteMemo(request, memo_id):
    Memo.objects.filter(id=memo_id).delete()
    return redirect('memos#.views.Inbox')

def encryptBody(text, publicRKey):
    encKey = RSA.importKey(publicRKey)
    return encKey.encrypt(text.encode('utf-8'), 32)

def decryptBody(text, rKey):
    print("This is rKEY: ", rKey)

    decKey = RSA.importKey(rKey)
    print("THIS IS AFTER DECKEY")
    print("Imported Key: "+ str(decKey))
    return decKey.decrypt(text.decode('utf-8'))