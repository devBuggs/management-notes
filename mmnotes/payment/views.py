from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from .models import Transaction
from .paytm import generate_checksum, verify_checksum
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# import models
from accounts.models import UserContact, UserSubscription, Course, SubscriptionPack

# import Views 
from accounts.views import profile_view
from courseapp.views import dashboard_view

UnlimitedAccess = SubscriptionPack.objects.get(subscription = "UnlimitedAccess")

@login_required
def initiate_payment(request):
    if request.method == "GET":
        userName = str(request.user.username)
        userContactInfo = UserContact.objects.get(username=userName).contact_number 
        orderAmount = '200'
        orderCurrency = 'INR'
        orderNote = 'Enroll Course Payment'
        customerName = request.user.first_name +' '+ request.user.last_name
        customerPhone = str(userContactInfo)
        customerEmail = request.user.email
        courses = Course.objects.all()
        postData = {
            "orderAmount" : orderAmount,
            "orderCurrency" : orderCurrency,
            "orderNote" : orderNote,
            "customerName" : customerName,
            "customerPhone" : customerPhone,
            "customerEmail" : customerEmail,
        }
        context = {
            'layout': 0,
            'footer': 0,
            'payment': postData,
            'courses': courses
        }
        return render(request, 'payment/pay.html', context)
    try:
        amount = int(request.POST['amount'])
        course = request.POST['course']
        userCourse = Course.objects.get(pk=course)
        user = request.user
        if user is None:
            raise ValueError
        auth_login(request=request, user=user)
    except:
        return render(request, 'payment/pay.html', context={'error': 'Wrong Accound Details or amount'})

    transaction = Transaction.objects.create(made_by=user, amount=amount)
    transaction.save()
    merchant_key = settings.PAYTM_SECRET_KEY

    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(transaction.made_by.email)),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
    )
    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)

    transaction.checksum = checksum
    transaction.save()

    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    return render(request, 'payment/redirect.html', context=paytm_params)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        paytm_checksum = ''
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            print("Checksum Matched")
            received_data['message'] = "Checksum Matched"
            return render(request, 'payment/callback.html', context=received_data)
        else:
            print("Checksum Mismatched")
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'payment/callback.html', context=received_data)
        return render(request, 'payment/callback.html', context=received_data)

@login_required
def paymentCallback(request):
    if request.method == "POST":
        user = request.user
        received_data = dict(request.POST)
        if received_data:
            for key,value in received_data.items():
                print("--------> ", key, " : ", value)
            if received_data['STATUS'] and received_data['BANKTXNID']:
                currentUserSubs = UserSubscription.objects.get(username = user.id)
                if str(currentUserSubs.subscription_details) == "NoAccess":
                    currentUserSubs.subscription_details = UnlimitedAccess
                    currentUserSubs.save()
        else:
            raise ValueError("Payment before enrollment!")
        courses = Course.objects.all()
        context = {
            'layout': 0,
            'footer': 0,
            'courses': courses,
            'subscription': str(currentUserSubs.subscription_details),
        }
        return render(request, 'payment/test.html', context)
    else:
        user = request.user
        currentUserSubs = UserSubscription.objects.get(username = user.id)
        courses = Course.objects.all()
        context = {
            'layout': 0,
            'footer': 0,
            'courses': courses,
            'subscription': str(currentUserSubs.subscription_details)
        }
        return render(request, 'payment/test.html', context)

@login_required()
def enrollmentCourse(request):
    if request.method == 'POST':
        user = request.user
        course = request.POST['course']
        if course:
            currentUserSubs = UserSubscription.objects.get(username = user.id)
            enrollmentCourse = Course.objects.get(id=course)
            currentUserSubs.subject_details = enrollmentCourse
            currentUserSubs.save()
            return redirect(dashboard_view)
        else:
            raise ValueError("Something went wrong.. ")
    return HttpResponse("<h1> Enrollment Updating.. please wait, whille we're working on your account.. </h1>")
            