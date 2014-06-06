# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article, UserProfile
from blog.forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
import sha, random
from datetime import datetime, timedelta
from django.core.mail import send_mail
# Create your views here.


def home(request):
    """ Afficher tous les articles """
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'last_articles': articles})


def view_article(request, id_article, slug):
    """ Afficher un article """
    article = get_object_or_404(Article, id=id_article)
    return render(request, 'blog/view_article.html', {'article': article})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            timelapse = datetime.today() + timedelta(2)
            salt = sha.new(str(random.random())).hexdigest()[:5]
            key= sha.new(salt+user.username).hexdigest()
            profile = UserProfile(user=user,key_expires=timelapse,activation_key=key)
            profile.save()
            send_confirmation(user.email,key)
            return redirect("blog.views.home")
    form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

def confirmation(request,key):
    profile = UserProfile.objects.filter(activation_key=key)

    return render(request, 'blog/confirmation.html')


def send_confirmation(email,key):
    url = reverse('blog.views.confirmation',kwargs={'key': key})
    subject = "no-reply, email confirmation"
    body = """
    Bonjours, merci de vous être enregistré sur keltorin.com, pour confirmer votre addresse email
    veuillez cliquer sur ce lien : %s. Ce lien sera actif pendant 48 heures""" % url
    send_mail(subject, body, 'keltorin@keltorin.com', [email])
