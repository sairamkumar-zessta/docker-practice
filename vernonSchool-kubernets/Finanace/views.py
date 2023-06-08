from django.shortcuts import render
from django.http import HttpResponse
from .forms import FeePayForm
from Admissions.views import home
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def fee_pay(request):
    form={'feepay' : FeePayForm}
    if request.method == 'POST':
        form = FeePayForm(request.POST)
        if form.is_valid(): 
            n = form.cleaned_data['name'] 
            c = form.cleaned_data['Class'] 
            a = form.cleaned_data['amount']

            print("Hi {} you are payment of {} is successful".format(form.cleaned_data['name'],form.cleaned_data['amount']))
            # dict = {"name" : n, "amount" : a, "class" : c}
            # return render(request,'index.html',dict)
            resp = HttpResponse('<h1> Your transaction is successful... </h1>')
            # resp.set_cookie("name",n) 
            # resp.set_cookie("class",c)
            # resp.set_cookie("amount",a)
            request.session['name'] = n;
            request.session['class'] = c;
            request.session['amount'] = a;
            return resp
    return render(request,'finance/fee_pay.html',form)

def fee_paid(request):
    # retrieve values from hidden variables
    # n = request.GET.get('nm')
    # a = request.GET.get('am')
    # c = request.GET.get('cl')
    # dict = {"name" : n, "amount" : a, "class" : c ,"status" : "Success"}
    # return render(request,'finance/receipt.html',dict) 
    return render(request,'finance/receipt.html') 

def fee_due(request):
    return HttpResponse('<h1> This is Fee due view section </h1> <h3> You can get details of who not paid fee </h3>')