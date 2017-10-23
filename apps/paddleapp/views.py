from django.shortcuts import render, HttpResponse, redirect
def index(request):
    
    return render(request, "paddleapp/index.html")

def buy(request):
    try:
        request.session['counter']
    except KeyError:
        request.session['counter'] = 0

    

    request.session['counter'] += int(request.POST['quantity'])
    
    price = {
        "1" : 1429.00,
        "2" : 1890.00,
        "3" : 1543.00,
        "4" : 1429.00,
        "5" : 1890.00,
        "6" : 1543.00,
    }

    quantity = request.POST['quantity']
    product = request.POST['product']
    request.session['total'] = int(quantity) * price[product]


    if 'total_purchase' not in request.session:
        request.session['total_purchase'] = request.session["total"]

    else:
        request.session['total_purchase'] += request.session['total'] 
        
        
    request.session.modified = True
    return redirect('/result')

def result(request):
    return render("paddleapp/checkout.html")






################################LOGIN REGISTRATION#####################





def login(request):
    return render(request, 'paddleapp/login.html')




def create(request):
    errors= User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/')

    User.objects.create(
        first_name= request.POST['first_name'],
        last_name= request.POST['last_name'],
        email= request.POST['email'],
    )
    return redirect('/')

################################LOGIN REGISTRATION#####################