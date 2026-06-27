"""
URL configuration for main_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import Settings, settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ind),
    path('user.html',views.user_register),
    path('prof',views.profile),
    path('addm',views.admi),
    path('profi',views.profile1),
    path('turf.html',views.turf_reg),
    path('login.html',views.log),
    path('about.html',views.about),
    path('ad',views.adm),
    path('delete', views.delete),
    path('update', views.update),

    path('forgot', views.forgot_password, name="forgot"),
    path('reset/<token>', views.reset_password, name='reset_password'),
    path('userpro',views.userprof),
    path('chpass',views.chpass),
    path('chpassword',views.changepass),
    path('logout', views.logout),
    path('userup',views.upuser),
    path('userupdate',views.userupdate),
    path('lb', views.trf),
    path('profile',views.prof),
    path('usrnm',views.tusrchg),
    path('uptrf',views.tupdate),
    path('usrchp',views.changepass),
    path('vturf',views.vturf),
    path('deleteturf',views.deleteturf),
    path('turfwarning', views.warning),
    path('turfwar',views.turfwarning),
    path('usrnmup',views.usrnamechg),
    path('ownr',views.owner),
    path('upownr',views.updtonr),
    path('user',views.usr),
    path('locfil.html',views.locfil),
    path('bkslot',views.bookslot),
    path('det/<a>',views.details),


    path('cont',views.cont),
    path('adviewcon', views.advicont, name='adviewcon'),
    path('send_reply', views.send_reply, name='send_reply'),

    path('book/<str:turf_name>/', views.book_turf, name='book_turf'),
    path('get_slots/<int:turf_id>/', views.get_slots, name='get_slots'),
    path('payment', views.make_payment, name='make_payment'),
    path('success', views.payment_success, name='payment_success'),
    path('view_bookings/', views.view_bookings, name='view_bookings'),
    path('pay',views.pay),
    path('turf_view_bookings/', views.turf_view_bookings, name='turf_view_bookings'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('vbook/', views.adm_view_bing_hstry, name='view_booking_history'),

































]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
