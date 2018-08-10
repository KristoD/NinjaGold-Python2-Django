from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'game_list' not in request.session:
        request.session['game_list'] = []
    return render(request, 'game/index.html')

def process(request, location):
    # strftime("%b %d, %Y", gmtime()),
    #     "time" : strftime("%H:%M %p", gmtime())
    if request.method == "POST":
        if location == "farm":
            gold = random.randint(10,20)
        if location == "cave":
            gold = random.randint(5,10)
        if location == "house":
            gold = random.randint(2,5)
        if location == "casino":
            gold = random.randint(-50,50)
            if gold > 0:
                gameStr = ("won", "You entered a casino and won " + str(gold) + " gold. Not sure how, I rigged the machines... (" + strftime("%Y/%m/%d %-H:%M %p", gmtime()) + ")")
            elif gold < 0:
                gameStr = ("lose", "You entered a casino and lost " + str(gold) + " gold. LuL git gud son. (" + strftime("%Y/%m/%d %-H:%M %p", gmtime()) + ")")
            else:
                gameStr = ("black", "You entered a casino and came out even... Noobs luck. (" + strftime("%Y/%m/%d %-H:%M %p", gmtime()) + ")")
        if location != "casino":
            gameStr = ("black", "You entered a " + location + " and somehow earned " + str(gold) + " gold. That's videogame logic for ya. (" + strftime("%Y/%m/%d %-H:%M %p", gmtime()) + ")")
        request.session['gold'] += gold
        new_list = request.session['game_list']
        new_list.append(gameStr)
        request.session['game_list'] = new_list
        return redirect('/')
    else:
        redirect('/')

def reset(request):
    if request.method == "POST":
        request.session.clear()
        return redirect('/')