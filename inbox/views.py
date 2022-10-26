from nturl2path import url2pathname
# import instance as instance
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .forms import ContactForm, AddSpamWordsForm
from filter.utils import email_check, ip_check, get_ip, word_check, add_spammer
from django.contrib import messages
from django.shortcuts import render
from filter.models import BlockedWords
from .models import Messages


#Create your views here.
def homePage(request):
    template = 'index.html'
    return render(request, template)


def guestPage(request):
    template = 'guest_page.html'
    return render(request, template)

@permission_required('admin.can_add_log_entry')
def adminPage(request):
    template = 'admin/base_cite.html'
    return render(request, template)

def contact(request):
    template = 'contact.html'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                instance = form.save(commit=False)
                instance.ip_address = get_ip(request)
                if email_check(instance.email):
                    messages.warning(request, 'You are in the spammers list')
                elif ip_check(instance.ip_address):
                    messages.warning(request, 'Your IP adress is in blocked list')
                elif word_check(instance.message):
                    messages.warning(request, 'You\'ve used spam word')
                else:
                    instance.save()
                    messages.success(request, "We have received your email, and we will respond soon")
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, template, context)

@permission_required('admin.can_add_log_entry')
def message_list(request):
    template = "message_list.html"
    items = Messages.objects.all()

    if request.POST:
        add_spammer(request.POST['email'], request.POST['ip_address'])
        spammer = Messages.objects.filter(email=request.POST['email'], ip_address=request.POST[
            'ip_address'])
        spammer.delete()
    context = {
        'items': items,
    }
    return render(request, template, context)

@permission_required('admin.can_add_log_entry')
def message_detail(request, pk):
    template = "message_detail.html"
    item = get_object_or_404(Messages, pk=pk)
    if request.POST:
        add_spammer(request.POST['email'], request.POST['ip_address'], request.POST['blocked_message'])
        spammer = ContactForm.objects.filter(email=request.POST['email'], ip_address=request.POST[
            'ip_address'], blocked_message=request.POST['blocked_message'])
        spammer.delete()
        return redirect('message_list')

    context = {
        'item': item,
    }
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def add_spam_word(request, pk):
    template = "add_spam_word.html"

    item = get_object_or_404(Messages, pk=pk)
    words = item.message.split()

    if request.method == "POST":
        form = AddSpamWordsForm(request.POST)
        form.fields['spam_words'].choices = [(i, i) for i in words]
        for word in request.POST.getlist('spam_words'):
            if not BlockedWords.objects.filter(word=word).exists():
                new_word = BlockedWords(word=word)
                new_word.save()
    else:
        form = AddSpamWordsForm()
        form.fields['spam_words'].choices = [(i, i) for i in words]
    context = {
        'item': item,
        'form': form,
    }
    return render(request, template, context)
