from django.urls import path
from . import views
urlpatterns=[
    path("",views.index),
    path("adminlogin/",views.adminlogin),
    path("admincheck/",views.admincheck),
    path("admin_homepage/",views.admin_homepage),
    path("loginform/",views.loginform),
    path("addcategory/",views.addcategory),
    path("savecategory/",views.savecategory),
    path("viewcategory/",views.viewcategory),
    path("addpets/",views.addpets),
    path("adpets_save/",views.adpets_save),
    path("view_pets/",views.view_pets),
    path("pets__/",views.pets__),
    path("view_singleimage/<id>",views.view_singleimage),
    path("ordersummery/<id>",views.ordersummery),
    path("registration_login/",views.registration_login),
    path("registration_login_save/",views.registration_login_save),
    path("check_log/",views.check_log),
    path("paymenthandler/",views.paymenthandler),
    path("user_logout/",views.user_logout),
    path("my_orders/",views.my_orders),
    path("view_pet_booking/",views.view_pet_booking),
    path("add_prods/",views.add_prods),
    path("view_prods/",views.view_prods),
    path("add_prods_save/",views.add_prods_save),
    path("edit_product/<id>",views.edit_product),
    path("update_product/<id>",views.update_product),
    path("products_view/",views.products_view),
    path("view_singleimage_product/<id>",views.view_singleimage_product),
    path("adddoctors/", views.adddoctors),
    path("save_dotrs_name/", views.save_dotrs_name),
    path("viewdoctors/", views.viewdoctors),
    path("doctors_view/", views.doctors_view),
    path("view_singleimage_doctors/<id>", views.view_singleimage_doctors),
    path("take_appoinment/<id>", views.take_appoinment),
    path("view_appoinment/", views.view_appoinment),
    path("appoinment_save/", views.appoinment_save),
    path("view_my_products/", views.view_my_products),
    path("view_booking_appoinments/", views.view_booking_appoinments),
    path("admin_view_pets/", views.admin_view_pets),
    path("admin_products_view/", views.admin_products_view),
    path("ordersummery_product/<id>",views.ordersummery_product),
    path("paymenthandler1/",views.paymenthandler1),
    path("about/",views.about),
    path("services/",views.about),
    path("contact/",views.about)
]
