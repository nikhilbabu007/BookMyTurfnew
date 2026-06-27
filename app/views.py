
from django.contrib.auth import login
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from.models import *
import razorpay
from django.contrib import messages



from datetime import datetime, date, timedelta

from django.utils import timezone
from datetime import timedelta, datetime
from django.utils.crypto import get_random_string
from  django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# Create your views here.
def ind(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')


def admi(request):
        d = turf.objects.filter(action='pending')
        d3 = turf.objects.filter(action='confirm')
        d5 = contact_admin.objects.filter(status='send')
        d7 = Payment.objects.filter(payment_status='Completed')
        d8 = d7.count()
        pending_count = d.count()
        d4 = d3.count()
        d6 = d5.count()
        return render(request,'admin.html',{'pending_count': pending_count,'d4':d4,'d6':d6,'d8':d8})

def usr(request):
    return render(request,'user.html')
def profile(request):
    if 'uid' in request.session:
        b = request.session['uid']
        d = user.objects.filter(username=b)
        data = turf.objects.filter(action='confirm')
        s = set()
        for i in data:
            s.add(i.location)
        l = list(s)
        return render(request,'user.html',{'r':d,'r1':l})
    else:
        return render(request,'login.html')
def profile1(request):
    if 'tid' in request.session:
        a=request.session['tid']
        d = turf.objects.filter(username=a)
        return render(request, 'turf.html',{'d':d})
    else:
        return render(request,'login.html')


def user_register(request):
    if request.method=='POST':
        a=request.POST['n1']
        c = request.POST['n3']
        b = request.POST['n2']
        d = request.POST['n4']
        e = request.POST['n5']
        data=user.objects.filter(username=b)
        t = user.objects.filter(email=c)
        if list(data)==[]:
            if list(t)==[]:
                d1=user.objects.create(name=a,username=b,email=c,phno=d,password=e)
                d2=login.objects.create(username=b,password=e,status=1)
                d1.save()
                d2.save()
                return render(request,'index.html')
            else:
               url = 'user.html'
               msg = '''<script>alert('email already exist')
                                        window.location='%s'</script>''' % (url)
               return HttpResponse(msg)
               return redirect(user_register)
        else:
             url = 'user.html'
             msg = '''<script>alert('username already exist')
                        window.location='%s'</script>''' % (url)
             return HttpResponse(msg)
             return redirect(user_register)
    else:
        return render(request,'uregister.html')



def turf_reg(request):
    if request.method=='POST':
        a=request.POST['n1']
        data=user.objects.filter(name=a)
        if list(data)==[]:
            b = request.POST['n2']
            c = request.POST['n3']
            d = request.POST['n4']
            e = request.POST['n5']
            f = request.POST['n6']
            g = request.POST['n7']
            h = request.FILES['n8']
            i = request.POST['n9']
            j= int(request.POST['n10'])
            k = request.POST['n11']
            l = request.POST['n12']
            m = request.POST['n13']
            n = request.POST['n14']
            o = request.FILES['n15']
            p = request.FILES['n16']
            q = request.POST['n17']
            r = int(request.POST['n18'])
            s = int(request.POST['n20'])
            u = int(request.POST['n21'])
            v = int(request.POST['n22'])

            z = turf.objects.filter(username=b)
            t = turf.objects.filter(email=g)
            if list(z)==[]:
                if list(t)==[]:
                             d1=turf.objects.create(name=a,username=b,address=c,location = d,owner = e,time=f,email = g, photo=h, password=i, phno=j,action='pending',pricing=k ,turf_type=l,surface_type=m, lighting=n, license=o, owner_image=p, owner_email=q, owner_phno = r,s_time=s, e_time=u, no_of_slots=v)
                             d2=login.objects.create(username=b,password=i,status=2)
                             d1.save()
                             d2.save()

                             return render(request, 'login.html')
                else:
                       url = 'turf.html'
                       msg = '''<script>alert('email already exist')
                                             window.location='%s'</script>''' % (url)
                       return HttpResponse(msg)

            else:
                 url = 'turf.html'
                 msg = '''<script>alert('username already exist')
                               window.location='%s'</script>''' % (url)
                 return HttpResponse(msg)


    else:
        return render(request, 'turfregister.html')

def log(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        try:
            if a =='nikhil' and b=='123admin':
                return redirect(admi)
            c = login.objects.get(username=a)
            if c.password == b:
                if c.status==1 :
                  request.session['uid'] = a
                  return redirect(profile)
                elif c.status==2:
                    f = turf.objects.get(username=a)
                    if f.action == 'confirm':
                        request.session['tid'] = a
                        return redirect(profile1)
                    else:
                        messages.info(request, 'your request is processing...you can login once your request is being approved by the admin!')
                        return render(request,'login.html')

            else:
                messages.info(request, 'login failed,password incorrect...')
                return render(request, 'login.html')
        except Exception:
            messages.info(request, 'login failed,incorrect username...')
            return render(request, 'login.html')
    else:
        return render(request,'login.html')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            u = user.objects.get(email=email)
        except:
            messages.info(request,"Email id not registered")
            return redirect(forgot_password)

        token = get_random_string(length=4)
        PasswordReset.objects.create(user=u, token=token)

        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        try:
            send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}','settings.EMAIL_HOST_USER', [email],fail_silently=False)

        except:
            messages.info(request,"Network connection failed")
            return redirect(forgot_password)

    return render(request, 'forgot.html')

def reset_password(request, token):

    password_reset = PasswordReset.objects.get(token=token)

    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('cpassword')
        if repeat_password == new_password:
            u = password_reset.user.username
            login.objects.filter(username=u).update(password=new_password)


            return redirect(login)
    return render(request, 'reset.html',{'token':token})

def userprof(request):
    if  request.method=='GET':
        a = request.session['uid']
        d = user.objects.filter(username=a)
        return render(request, 'userprofile.html', {'r': d})
    else:
        return render(request,'user.html')
#user
def chpass(request):
    if request.method=='POST':
        x=request.POST['n']
        y=request.POST['n1']
        z=request.POST['n2']
        d=login.objects.filter(username=x)
        d1 = login.objects.filter(password=y)
        if list(d) != []:
            if list(d1) != []:
                d.update(password=z)
                return render(request, 'login.html')
            else:
                messages.info(request, 'incorrect password!...please enter correct password to proceed')
                return render(request, 'changepassword.html')
        else:
            messages.info(request, 'incorrect username!...please enter correct username to proceed')
            return render(request, 'changepassword.html')

    else:
        return render(request, 'changepassword.html')

#turf
def changepass(request):
    if request.method=='POST':
        x=request.POST['n']
        y=request.POST['n1']
        z=request.POST['n2']
        d=login.objects.filter(username=x)
        d1=login.objects.filter(password=y)
        if list(d)!=[]:
            if list(d1)!=[]:
                d.update(password=z)
                return render(request,'login.html')
            else:
                messages.info(request,'incorrect password!...please enter correct password to proceed')
                return render(request, 'changepass.html')
        else:
            messages.info(request, 'incorrect username!...please enter correct username to proceed')
            return render(request, 'changepass.html')

    else:
        return render(request,'changepass.html')


def logout(request):
    if 'uid' in request.session:
        request.session.flush()
        return render(request,'index.html')
    elif 'tid' in request.session:
        request.session.flush()
        return render(request,'index.html')
    else:
        return render(request,'index.html')

def upuser(request):
    if request.method=='POST':
        x=request.POST['c1']
        d=user.objects.filter(username=x)
        return render(request,'updateuser.html',{'r':d})
    else:
        return render(request,'updateuser.html')

def userupdate(request):
    if request.method=='POST':
        a = request.POST['w']
        b = request.POST['a1']
        g = int(request.POST['a3'])
        e = request.POST['a4']
        d = user.objects.filter(username=a)
        d.update(name=b,phno=g,email=e)
        return redirect(userprof)
    else:
        return render(request,'updateuser.html')

def adm(request):
    if request.method=='GET':
         d=turf.objects.filter(action='pending')
         pending_count = d.count()
         return render(request,'request.html',{'r':d, 'pending_count': pending_count})
    else:
        return render(request,'admin.html')

def delete(request):
    if request.method=='POST':
        a = request.POST['b2']
        d = turf.objects.filter(name=a)
        d1 = turf.objects.get(name=a)
        d2= d1.username
        d3=login.objects.filter(username=d2)
        d4=d1.email
        d5=d1.owner_email
        d.delete()
        d3.delete()
        send_mail('Rejected', 'you turf has been  rejected by the Website BookMyTurf. Please register with all the propper details required',
                  'settings.EMAIL_HOST_USER', [d4,d5], fail_silently=False)

        return redirect(adm)
    else:
        return render(request, 'request.html')

def update(request):
    if request.method=='POST':
        a = request.POST['b1']
        d = turf.objects.filter(name=a)
        d1 = turf.objects.get(name=a)
        d2 = d1.email
        d3 = d1.owner_email
        d.update(action='confirm')
        send_mail('ACCEPTED!', 'your turf has been  registered to the Website BookMyTurf. You can now login using your registered username and password',
                  'settings.EMAIL_HOST_USER', [d2,d3], fail_silently=False)

        return redirect(adm)
    else:
        return render(request,'request.html')


def trf(request):
    if request.method=='GET':
         d=turf.objects.filter(action='confirm')
         return render(request,'turf.html',{'r':d})
    else:
        return render(request,'index.html')

def prof(request):
    if request.method=='GET':
        a = request.session['tid']
        d = turf.objects.filter(username=a)
        return render(request, 'profile.html', {'r': d})
    else:
        return render(request,'turf.html')

def tupdate(request):
    if request.method=='POST':
        a=request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        d = request.POST['n4']
        e = request.POST['n5']
        f = request.POST['n6']
        g = request.POST['n7']
        #h = request.FILES['n8']
        j = int(request.POST['n10'])
        k = request.POST['n11']
        l = request.POST['n12']
        m = request.POST['n13']
        n = request.POST['n14']
        #o = request.FILES['n15']
        #p = request.FILES['n16']
        q = request.POST['n17']
        r = int(request.POST['n18'])
        t=turf.objects.filter(username=b)

        t.update(name=a,address=c,location = d,owner = e,time=f,email = g, phno=j,pricing=k ,turf_type=l,surface_type=m, lighting=n, owner_email=q, owner_phno = r)

        return redirect(prof)
    else:
        a = request.session['tid']
        data = turf.objects.filter(username=a)
        return render(request,'updateturf.html',{'r':data})

#turf username change
def tusrchg(request):
    if request.method=='POST':
        x=request.POST['n1']
        a=request.POST['n2']
        d=login.objects.filter(username=x)
        d1=turf.objects.filter(username=x)
        if list(d)!=[]:
            d.update(username=a)
            d1.update(username=a)
            return render(request,'login.html')
        else:
            messages.info(request,'username error...please enter the correct username')
            return redirect(tusrchg)

    else:
        return render(request,'tusrupdate.html')

#admin view turf
def vturf(request):
    if request.method=='GET':
         d=turf.objects.filter(action='confirm')
         d1=turf.objects.filter(action='pending')
         pending_count = d1.count()
         return render(request,'vturf.html',{'r':d, 'pending_count':pending_count})
    else:
        return render(request,'turf.html')

#admin delete turf
def deleteturf(request):
    if request.method=='POST':
        a = request.POST['b2']
        d = turf.objects.get(username=a)
        d1 = login.objects.get(username=a)
        b=d.email
        b1=d.owner_email
        d.delete()
        d1.delete()
        send_mail('Removed','you turf has been  removed from the Website BookMyTurf',
                  'settings.EMAIL_HOST_USER', [b,b1], fail_silently=False)
        return redirect(vturf)
    else:
        return render(request,'vturf.html')

#admin Warning turf due to feedback
def warning(request):
    if request.method=='POST':
        x=request.POST['b3']
        y=request.POST['b2']
        d=turf.objects.filter(name=y,email=x)
        return render(request,'warning.html',{'r':d})
    else:
        return render(request, 'warning.html')

def turfwarning(request):
    if request.method=='POST':
        b = request.POST['n']
        c = request.POST['n1']
        send_mail('Warning Message', c,'settings.EMAIL_HOST_USER', [b], fail_silently=False)
        return redirect(turfwarning)
    else:
         return render(request, 'warning.html')

def usrnamechg(request):
    if request.method=='POST':
        x=request.POST['n1']
        a=request.POST['n2']
        d=login.objects.filter(username=x)
        d1=user.objects.filter(username=x)
        if list(d)!=[]:
            d.update(username=a)
            d1.update(username=a)
            return render(request,'login.html')
        else:
            messages.info(request, 'username error...please enter the correct username')
            return redirect(usrnamechg)

    else:
        return render(request,'usrnameupdate.html')
#contact to  admin
def cont(request):
    if request.method == 'POST':
        w = request.POST['n1']
        x = request.POST['n2']
        y = request.POST['n3']
        z = request.POST['n4']
        data=contact_admin.objects.create(name=w,email=y,contact_no=x,message=z, status='send')

        data.save()
        return redirect(cont)
    else:
        return render(request,'contact.html')
#admin-view-complaint
def advicont(request):
    d = contact_admin.objects.filter(status='send')
    return render(request, 'advicont.html', {'r': d})
#admin send reply
def send_reply(request):
    if request.method == 'POST':
        msg_id = request.POST['msg_id']
        reply_text = request.POST['reply']
        email = request.POST['email']

        try:
            contact_entry = contact_admin.objects.get(id=msg_id)
            # Send email to user
            send_mail(
                subject="Reply from BookMyTurf Admin",
                message=reply_text,
                from_email='settings.EMAIL_HOST_USER',
                recipient_list=[email],
                fail_silently=False,
            )
            # Update message status
            contact_entry.status = 'replied'
            contact_entry.save()

        except contact_admin.DoesNotExist:
            messages.error(request, "Message not found.")

        return redirect('adviewcon')  # redirect back to the feedback list
#user view owner
def owner(request):
    if request.method == 'GET':
        a = request.session['tid']
        y= turf.objects.filter(username=a)
        return render(request,'owner.html',{'y':y})
    else:
        return render(request, 'owner.html')

def updtonr(request):
    if request.method =='POST':
        a = request.POST['n4']
        b  = request.POST['n1']
        c = request.POST['n2']
        d = request.POST['n3']
        #e = request.POST['n4']
        f = turf.objects.filter(username=a)
        f.update(owner=b,owner_email=c,owner_phno=d)
        return redirect(owner)
    else:
        a = request.session['tid']
        data = turf.objects.filter(username=a)
        return render(request,'updtonr.html',{'r':data})


#turf location search
def locfil(request):
    if request.method == 'POST':
        x = request.POST['f1']
        d = turf.objects.filter(location=x,action='confirm')
        return render(request, 'turfdetails.html', {'r':d})
    else:
       return render(request, 'user.html')

def bookslot(request):
        data = turf.objects.filter(action='confirm')
        return render(request, 'viewturfdetails.html', {'r': data})



def details(request,a):
        request.session['sid'] = a
        d = turf.objects.filter(name=a)
        return render(request, 'xxx.html', {'r': d})

#chatgpt
# @login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from datetime import datetime, time
import json
from django.contrib import messages
from .models import turf, Booking, Payment

# SLOT AVAILABILITY
def get_slots(request, turf_id):
    t = get_object_or_404(turf, id=turf_id)
    date_str = request.GET.get('date')
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

    slots = []
    for h in range(t.s_time, t.e_time):
        start = time(h, 0)
        end = time(h + 1, 0)
        label = f"{start.strftime('%I:%M %p')} - {end.strftime('%I:%M %p')}"
        booked = Booking.objects.filter(turf=t, date=date_obj, time=label).exists()
        slots.append({"time": label, "booked": booked})

    return JsonResponse({"slots": slots})


# BOOK TURF
def book_turf(request, turf_name):
    # Get the turf the user wants to book
    t = get_object_or_404(turf, name=turf_name)

    # Check if user is logged in via session
    username = request.session.get('uid')
    if not username:
        messages.error(request, "Please log in to book a turf.")
        return redirect('login')  # redirect to your login view name

    # Get user details from your user model
    try:
        u = user.objects.get(username=username)
    except user.DoesNotExist:
        messages.error(request, "User not found. Please log in again.")
        return redirect('login')

    # If booking form is submitted
    if request.method == 'POST':
        date = request.POST.get('selected_date')
        slots_json = request.POST.get('selected_slots')
        selected_slots = json.loads(slots_json) if slots_json else []

        # Validate slot selection
        if not selected_slots:
            messages.error(request, "Please select at least one slot.")
            return redirect('book_turf', turf_name=t.name)

        total_amount = len(selected_slots) * t.pricing

        # Store payment/booking data temporarily in session
        request.session['payment_data'] = {
            'turf_id': t.id,
            'turf_name': t.name,
            'turf_location': t.location,
            'date': date,
            'slots': selected_slots,
            'amount': total_amount,
            'user_name': u.name,
            'user_email': u.email,
            'user_phone': u.phno,
        }

        return redirect('make_payment')  # or your payment page

    # Render booking page with turf + user details
    return render(request, 'turf_booking.html', {
        'turf': t,
        'user': u
    })


# PAYMENT PAGE

def make_payment(request):
    # Retrieve session data
    payment_data = request.session.get('payment_data')

    if not payment_data:
        messages.error(request, "No booking data found.")
        return redirect('home')

    # Get the turf
    t = get_object_or_404(turf, id=payment_data['turf_id'])

    # Simulate a payment (POST means user confirmed payment)
    if request.method == 'POST':
        # ✅ Create Payment record first
        request.session['user'] = request.user.id
        request.session['turf_id'] = t.id
        request.session['user_name'] = payment_data['user_name']
        request.session['user_email'] = payment_data['user_email']
        request.session['user_phone'] = payment_data['user_phone']
        request.session['turf_name'] = t.name
        request.session['turf_location'] = t.location
        request.session['turf'] = payment_data['date']
        request.session['booked_slots'] = json.dumps(payment_data['slots'])
        request.session['amount'] = payment_data['amount']

        # ✅ Create Booking entries for each selected slot
        for slot in payment_data['slots']:
            # Prevent duplicate bookings for the same turf/date/slot
            Booking.objects.get_or_create(
                user=request.user,
                turf=t,
                date=payment_data['date'],
                time=slot
            )

        # ✅ Clear temporary session data
        if 'payment_data' in request.session:
            del request.session['payment_data']

        # ✅ Redirect to success page
        return redirect(pay)

    # Render payment confirmation page
    return render(request, 'payment.html', {
        'payment_data': payment_data,
        'turf': t
    })



# PAYMENT SUCCESS PAGE
def payment_success(request):
    u = request.session['user']
    t = request.session['turf_id']
    turf_data = turf.objects.get(id=t)
    user_data = user.objects.get(id=u)

    payment = Payment.objects.create(
        user=user_data,
        turf=turf_data,
        user_name=request.session['user_name'],
        user_email=request.session['user_email'],
        user_phone=request.session['user_phone'],
        turf_name=request.session['turf_name'],
        turf_location=request.session['turf_location'],
        booking_date=request.session['turf'],
        booked_slots=request.session['booked_slots'],
        amount=request.session['amount'],
        payment_status='Completed',
    )
    payment.save()


    user_email = payment.user_email
    user_name = payment.user_name
    turf_name = payment.turf_name
    booking_date = payment.booking_date
    booked_slots = payment.booked_slots
    amount = payment.amount

    subject = "BOOKED! Your Turf Slot is Confirmed 🎉"

    message = f"""
Hi {user_name},

Great news! Your turf booking is CONFIRMED ✔

📅 Date: {booking_date}
⏰ Slot: {booked_slots}
🏟 Turf: {turf_name}
💰 Amount Paid: ₹{amount}

Your payment has been successfully completed.

⚠ CANCELLATION POLICY:
You may cancel the booking ONLY up to **12 hours before the slot time**.

Thank you for booking with BookMyTurf! 🙌

Regards,
BookMyTurf Team
"""

    # send email
    send_mail(
        subject,
        message,
        'settings.EMAIL_HOST_USER',   # sender email
        [user_email],               # recipient
        fail_silently=False,
    )

    return render(request, 'payment_success.html')
# VIEW BOOKINGS
def login_view(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pwd = request.POST.get("password")

        try:
            log = login.objects.get(username=uname, password=pwd, status=1)
            request.session['uid'] = uname  # store username in session
            return redirect('profile')
        except login.DoesNotExist:
            return render(request, 'login.html', {'msg': 'Invalid credentials'})

    return render(request, 'login.html')

def view_bookings(request):
    if 'uid' not in request.session:
        return redirect('log')

    username = request.session['uid']

    logged_user = get_object_or_404(user, username=username)
    user_bookings = Payment.objects.filter(user_email=logged_user.email).order_by('-created_at')

    bookings_with_cancel = []

    for b in user_bookings:
        cancel_allowed = False
        try:
            slots = json.loads(b.booked_slots)
            first_slot = slots[0]
            start_time_str = first_slot.split(" - ")[0]
            slot_start_dt = datetime.strptime(start_time_str, "%I:%M %p")
            slot_datetime = datetime.combine(b.booking_date, slot_start_dt.time())
            slot_datetime = timezone.make_aware(slot_datetime)

            if timezone.now() < slot_datetime - timedelta(hours=12) and b.payment_status != "Cancelled":
                cancel_allowed = True
        except:
            cancel_allowed = False

        bookings_with_cancel.append({
            'booking': b,
            'cancel_allowed': cancel_allowed
        })

    context = {
        'bookings': bookings_with_cancel,
        'username': logged_user.name,
    }

    return render(request, 'view_bookings.html', context)

def pay(request):
    amount = request.session['amount']*100
    #request.session['amount'] = id
    order_currency = 'INR'
    client = razorpay.Client(
        auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    # cursor = connection.cursor()
    # cursor.execute(
    #     "update inspection_details set status='completed', fine_paid_date = curdate() where insp_id='" + str(
    #         id) + "' ")

    # payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    return render(request, "pay.html", {'r': amount})

#turf views booking

def turf_view_bookings(request):
    if 'tid' not in request.session:
        return redirect('log')  # Turf not logged in

    turf_username = request.session['tid']
    logged_turf = get_object_or_404(turf, username=turf_username)

    turf_name = logged_turf.name

    bookings = Payment.objects.filter(turf_name=turf_name).order_by('-created_at')

    bookings_with_status = []

    for b in bookings:
        cancel_allowed = False
        try:
            slots = json.loads(b.booked_slots)
            first_slot = slots[0]
            start_time_str = first_slot.split(" - ")[0]
            slot_start_dt = datetime.strptime(start_time_str, "%I:%M %p")
            slot_datetime = datetime.combine(b.booking_date, slot_start_dt.time())
            slot_datetime = timezone.make_aware(slot_datetime)

            if timezone.now() < slot_datetime - timedelta(hours=12) and b.payment_status != "Cancelled":
                cancel_allowed = True
        except:
            cancel_allowed = False

        bookings_with_status.append({
            'booking': b,
            'cancel_allowed': cancel_allowed
        })

    context = {
        'bookings': bookings_with_status,
        'turf_name': turf_name,
    }

    return render(request, 'turfviewbookings.html', context)
# cancellation
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime, timedelta
import json
from django.contrib import messages
from .models import Payment, Booking, turf
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, timedelta
from django.core.mail import send_mail
import json

def cancel_booking(request, booking_id):

    booking = get_object_or_404(Payment, id=booking_id)

    try:
        slots = json.loads(booking.booked_slots)
        first_slot = slots[0]


        start_time_str = first_slot.split(" - ")[0]


        slot_start_dt = datetime.strptime(start_time_str, "%I:%M %p")

        # Combine with booking date
        slot_datetime = datetime.combine(booking.booking_date, slot_start_dt.time())

        # Convert to timezone-aware
        slot_datetime = timezone.make_aware(slot_datetime)

    except Exception as e:
        messages.error(request, "Invalid slot format!")
        return redirect('view_bookings')

    now = timezone.now()

    # Check 12-hour rule
    if now > slot_datetime - timedelta(hours=12):
        messages.error(request, "Cancellation not possible. You must cancel at least 12 hours before your slot.")
        return redirect('view_bookings')

    # Free the slot in Booking table (slot becomes available)
    Booking.objects.filter(
        turf=booking.turf,
        date=booking.booking_date,
        time=first_slot
    ).delete()

    # Mark booking as cancelled
    booking.payment_status = "Cancelled"
    booking.save()

    # -----------------------------------
    # SEND EMAIL TO USER AFTER CANCELLATION
    # -----------------------------------

    subject = "Your Booking Has Been Cancelled"
    message = (
        f"Hello {booking.user_name},\n\n"
        f"Your turf booking slot from {first_slot} on {booking.booking_date} "
        f"has been successfully cancelled.\n\n"
        f"The amount ₹{booking.amount} has been refunded to your account.\n\n"
        f"Thank you for choosing BookMyTurf!"
    )

    send_mail(
        subject,
        message,
        'settings.EMAIL_HOST_USER',
        [booking.user_email],
        fail_silently=False,
    )

    messages.success(request, f"Booking cancelled successfully! Slot {first_slot} is now available.")

    return redirect('view_bookings')

def adm_view_bing_hstry(request):
    # Fetch all bookings ordered by newest first
    bookings = Payment.objects.all().order_by('-booking_date', '-created_at')
    return render(request, 'adm_view_bing_hstry.html', {'bookings': bookings})















