from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from .models import Transaction
from .paytm import generate_checksum, verify_checksum
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# import models
from accounts.models import UserContact, UserSubscription, Course


@login_required
def initiate_payment(request):
    if request.method == "GET":
        userName = str(request.user.username)
        userContactInfo = UserContact.objects.get(username=userName).contact_number 
        #orderId = str(request.user.first_name[0:3])+str(request.user.last_name[0:3])      #+str(userContactInfo[4:9])
        orderAmount = '200'
        orderCurrency = 'INR'
        orderNote = 'Enroll Course Payment'
        customerName = request.user.first_name +' '+ request.user.last_name
        customerPhone = str(userContactInfo)
        customerEmail = request.user.email

        # Course data
        courses = Course.objects.all()   #.in_bulk()
        print("--------------------", courses, "------------------------------")

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
        #username = request.user.username
        #password = request.POST['password']
        amount = int(request.POST['amount'])
        course = request.POST['course']
        print("---------------------------------------------", course, "---------------------------------------------")
        userCourse = Course.objects.get(pk=course)
        print("---------------------------------------------", userCourse, "---------------------------------------------")
        #user = authenticate(request, username=username, password=password)
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
            #print("---------------------------------------------", received_data, "-------------------------------------")
            # Upgrade UserAccount,  UserSubscription and give Access
            userUpgradeObject = UserAccountUpgrade(request.user, received_data)
            return render(request, 'payment/callback.html', context=received_data)
        else:
            print("Checksum Mismatched")
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'payment/callback.html', context=received_data)
        return render(request, 'payment/callback.html', context=received_data)



class UserAccountUpgrade:
    paymentData = {}
    txnid = ''

    def __init__(self, user, received_data):
        self.user = user
        self.paymentData = received_data
        print("--------------------- User Account Upgradeing --------------------------")
        print(self.paymentData)
        #print(type(self.paymentData))
        
        for key,value in received_data.items():
            #self.key = value
            print("------------ ", key, " : ", value)

        print(received_data['TXNID'])

        


