import razorpay
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
# Create your views here.
from django. contrib.auth import authenticate,login


from.models import *


def index(request):
    try:
        if request.session['pqr']:
            us=request.session['pqr']
            return render(request,"index.html",{"us":us})
    except:
        return render(request,"index.html")

def adminlogin(request):
    return render(request,"adminlogin.html")

def admincheck(request):
    if request.method=="POST":
        username=request.POST.get("u")
        password=request.POST.get("p")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/admin_homepage/")
        else:
            return redirect("/loginform/")

def admin_homepage(request):
    t_pet=tbl_adding_pets.objects.all().count()
    t_pdt=tbl_adding_products.objects.all().count()
    t_doc=tbl_dr.objects.all().count()

    return render(request,"admin_homepage.html",{"t_pet":t_pet,"t_pdt":t_pdt,"t_doc":t_doc})

def loginform(request):
    return render(request,"loginform.html")

def addcategory(request):
    return render(request,"addcategory.html")

def savecategory(request):
    d=tbl_category()
    d.name=request.POST.get('name')
    image=request.FILES['image']
    fs=FileSystemStorage()
    file=fs.save(image.name,image)
    url=fs.url(file)
    d.image=url
    d.description=request.POST.get('description')
    d.save()
    return redirect('/addcategory/')

def viewcategory(request):
    t=tbl_category.objects.all()
    return render(request,"viewcategory.html",{"t":t})

def addpets(request):
    return render(request,"addpets.html")

def adpets_save(request):
    m=tbl_adding_pets()
    m.category=request.POST.get('category')
    m.breed=request.POST.get('breed')
    m.stock=request.POST.get('stock')
    m.age=request.POST.get('age')
    m.gender=request.POST.get('gender')
    m.birthdate=request.POST.get('birthdate')
    pic=request.FILES['pic']
    ks=FileSystemStorage()
    file=ks.save(pic.name,pic)
    url=ks.url(file)
    m.pic=url
    m.characteristics = request.POST.get('characteristics')
    m.description = request.POST.get('description')
    m.price = request.POST.get('price')
    m.status=request.POST.get('status')
    m.save()
    return redirect('/addpets/')

def view_pets(request):
    j=tbl_adding_pets.objects.all()
    return render(request,"view_pets.html",{"j":j})

def pets__(request):
    try:
        if request.session['pqr']:
            us=request.session['pqr']
            q=tbl_adding_pets.objects.all()
            return render(request,"pets__.html",{"q":q,"us":us})
    except:
        q = tbl_adding_pets.objects.all()
        return render(request, "pets__.html",{"q":q})

def view_singleimage(request,id):
    try:
        if request.session['pqr']:
            us=request.session['pqr']
            wo=tbl_adding_pets.objects.get(id=id)
            return render(request,"view_singleimage.html",{"wo":wo,"us":us})

    except:
        wo = tbl_adding_pets.objects.get(id=id)
        return render(request, "view_singleimage.html",{"wo":wo})

razorpay_client = razorpay.Client(auth=('rzp_test_gtRapFlEoUFkrd', 'VdFzsxOMJXpbw24E7g9VhwxR'))

def ordersummery(request,id):
    try:
        if request.session['pqr']:
            us=request.session['pqr']
        wo = tbl_adding_pets.objects.get(id=id)
        total = int(wo.price) + 50
        currency = 'INR'
        amount = int(total) * 100

        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                           currency=currency,
                                                           payment_capture='0'))

        # order id of newly created order.
        razorpay_order_id = razorpay_order['id']
        callback_url = 'paymenthandler'

        # we need to pass these details to frontend.
        context = {}
        context['razorpay_order_id'] = razorpay_order_id


        context['razorpay_merchant_key'] = 'rzp_test_gtRapFlEoUFkrd'
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['callback_url'] = callback_url
        context['wo']=wo
        context['total']=total
        context["us"]=us


        return render(request,"ordersummery.html",context)
    except:
        return redirect("/registration_login/")

def registration_login(request):
    return render(request,"registration_login.html")

def registration_login_save(request):
    ty=tbl_register_login()
    ty.firstname=request.POST.get('firstname')
    ty.lastname=request.POST.get('lastname')
    ty.email=request.POST.get('email')
    ty.password=request.POST.get('password')
    ty.save()
    return redirect('/registration_login/')

def check_log(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    if tbl_register_login.objects.filter(email=email,password=password).exists():
        var=tbl_register_login.objects.get(email=email,password=password)
        request.session['pqr']=var.id
        return redirect('/')
    else:
        return redirect('/registration_login/')


def paymenthandler(request):
    d=request.POST.get("wo")
    print(d)
    data=tbl_adding_pets.objects.get(id=d)
    total=request.POST.get("total")

    razorpay_order_id = request.POST.get('order_id')

    payment_id = request.POST.get('payment_id', '')
    print('paymentid:', str(payment_id))

    signature = request.POST.get('razorpay_signature', '')

    params_dict = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_payment_id': payment_id,
        'razorpay_signature': signature
    }

    # verify the payment signature.

    print("res:")
    amount = int(total) * 100  # Rs. 200
    f=tbl_Booking_Pets()
    f.user_id=request.session['pqr']
    f.pet_id=data.id
    f.total=total
    f.save()
    razorpay_client.payment.capture(payment_id, amount)
    return redirect("/my_orders/")

def user_logout(request):
    del request.session['pqr']
    return redirect("/")

def my_orders(request):
    try:
        if request.session['pqr']:
            us = request.session['pqr']
            return render(request,"my_orders.html",{"us":us})
    except:
        return render(request, "my_orders.html")

def view_pet_booking(request):
    try:
        if request.session['pqr']:
            us = request.session['pqr']
            tr=tbl_Booking_Pets.objects.filter(user=request.session['pqr'])
            return render(request,"view_pet_booking.html",{'tr':tr,"us":us})
    except:
        return render(request, "view_pet_booking.html")


def add_prods(request):
    return render(request,"add_prods.html")

def add_prods_save(request):
    ms=tbl_adding_products()
    ms.category=request.POST.get('category')
    image=request.FILES['image']
    gs=FileSystemStorage()
    file=gs.save(image.name,image)
    url=gs.url(file)
    ms.image=url
    ms.product_name=request.POST.get('product_name')
    ms.price=request.POST.get('price')
    ms.save()
    return redirect('/add_prods/')

def view_prods(request):
    kro=tbl_adding_products.objects.all()
    return render(request,"view_prods.html",{"kro":kro})

def edit_product(request,id):
    data=tbl_adding_products.objects.get(id=id)
    return render(request, "edit_product.html", {"data": data})

def update_product(request,id):
    obs=tbl_adding_products.objects.get(id=id)
    obs.category=request.POST.get("category")
    obs.product_name=request.POST.get("product_name")
    obs.price=request.POST.get("price")
    obs.save()
    return redirect("/view_prods/")

def products_view(request):
    try:
        if request.session['pqr']:
            us=request.session['pqr']
            qi=tbl_adding_products.objects.all()
            return render(request,"products_view.html",{"qi":qi,"us":us})
    except:
        qi = tbl_adding_products.objects.all()
        return render(request, "products_view.html",{"qi":qi})

def view_singleimage_product(request,id):
    try:
        if request.session['rst']:
            usa=request.session['rst']
            wy=tbl_adding_pets.objects.get(id=id)
            return render(request,"view_singleimage_product.html",{"wy":wy,"usa":usa})

    except:
        wy = tbl_adding_products.objects.get(id=id)
        return render(request, "view_singleimage_product.html",{"wy":wy})

def adddoctors(request):
    return render(request,"adddoctors.html")

def save_dotrs_name(request):
    d=tbl_dr()
    d.doctors_name=request.POST.get('doctors_name')
    d.specialised = request.POST.get('specialised')
    image=request.FILES['image']
    fs=FileSystemStorage()
    file=fs.save(image.name,image)
    url=fs.url(file)
    d.image=url
    d.save()
    return redirect('/adddoctors/')

def viewdoctors(request):
    dr=tbl_dr.objects.all()
    return render(request,"viewdoctors.html",{"dr":dr})

def doctors_view(request):
    try:
        if request.session['pqr']:
            us=request.session['pqr']
            qi=tbl_dr.objects.all()
            return render(request,"doctors_view.html",{"qi":qi,"us":us})
    except:
        qi = tbl_dr.objects.all()
        return render(request, "doctors_view.html",{"qi":qi})

def view_singleimage_doctors(request,id):
    try:
        if request.session['rst']:
            us=request.session['rst']
            wys=tbl_dr.objects.get(id=id)
            return render(request,"view_singleimage_doctors.html",{"wys":wys,"us":us})

    except:
        wys = tbl_dr.objects.get(id=id)
        return render(request, "view_singleimage_doctors.html",{"wys":wys})

def take_appoinment(request,id):
    kr=tbl_appoinment.objects.get(id=id)
    return render(request,"take_appoinment.html",{"kr":kr})

def view_appoinment(request):
    kr=tbl_appoinment.objects.all()
    return render(request,"view_appoinment.html",{"kr":kr})

def appoinment_save(request):
    d=tbl_appoinment()
    d.name=request.POST.get('name')
    d.age = request.POST.get('age')
    d.birthdate = request.POST.get('birthdate')
    d.symptoms = request.POST.get('symptoms')
    d.district = request.POST.get('district')
    d.place = request.POST.get('place')
    d.save()
    return redirect('/')

def view_my_products(request):
    try:
        if request.session['pqr']:
            us = request.session['pqr']
            tr=tbl_adding_products.objects.filter(user=request.session['pqr'])
            return render(request, "view_my_products.html", {'tr':tr,"us":us})
    except:
        return render(request, "view_my_products.html")

def view_booking_appoinments(request):
    try:
        if request.session['pqr']:
            us = request.session['pqr']
            tr=tbl_appoinment.objects.filter(user=request.session['pqr'])
            return render(request, "view_booking_appoinments.html", {'tr':tr,"us":us})
    except:
        return render(request, "view_booking_appoinments.html")

def admin_view_pets(request):
    kr=tbl_Booking_Pets.objects.all()
    return render(request,"admin_view_pets.html",{"kr":kr})

def admin_products_view(request):
    kr=tbl_product_booking.objects.all()
    return render(request,"admin_products_view.html",{"kr":kr})

def ordersummery_product(request,id):
    try:
        if request.session['pqr']:
            us=request.session['pqr']
        wo = tbl_adding_products.objects.get(id=id)
        total = int(wo.price) + 50
        currency = 'INR'
        amount = int(total) * 100

        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                           currency=currency,
                                                           payment_capture='0'))

        # order id of newly created order.
        razorpay_order_id = razorpay_order['id']
        callback_url = 'paymenthandler1'

        # we need to pass these details to frontend.
        context = {}
        context['razorpay_order_id'] = razorpay_order_id


        context['razorpay_merchant_key'] = 'rzp_test_gtRapFlEoUFkrd'
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['callback_url'] = callback_url
        context['wo']=wo
        context['total']=total
        context["us"]=us


        return render(request,"ordersummery_product.html",context)
    except:
        return redirect("/registration_login/")

def paymenthandler1(request):
    d=request.POST.get("wo")
    print(d)
    data=tbl_adding_products.objects.get(id=d)
    total=request.POST.get("total")

    razorpay_order_id = request.POST.get('order_id')

    payment_id = request.POST.get('payment_id', '')
    print('paymentid:', str(payment_id))

    signature = request.POST.get('razorpay_signature', '')

    params_dict = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_payment_id': payment_id,
        'razorpay_signature': signature
    }

    # verify the payment signature.

    print("res:")
    amount = int(total) * 100  # Rs. 200
    f=tbl_product_booking()
    f.user_id=request.session['pqr']
    f.product_id=data.id
    f.address=request.POST.get("address")
    f.landmark=request.POST.get("Landmark")
    f.phone=request.POST.get("phone")
    f.save()
    razorpay_client.payment.capture(payment_id, amount)
    return redirect("/my_orders/")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"contact.html")
