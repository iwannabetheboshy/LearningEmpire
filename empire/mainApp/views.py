from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ContactForm
from django.contrib import messages
import json
import telebot
import os
from django.urls import reverse


BotToken=str(os.getenv('BotToken'))
bot=telebot.TeleBot(BotToken)
              
def index(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':        
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            messages.success(request, 'Ваша заявка успешно отправлена!')
            
            if phone[0] == '8' or phone[0] == '7':
                phone = '+7' + phone[1:]
                
            bot.send_message(5268041667, 'Заявка на обучение\nИмя: {0}\nТелефон: {1}\nПредмет: {2}'.format(name, phone, subject))
            return HttpResponseRedirect('./#contact')       
        
    return render(request, './index.html', {'form': form})