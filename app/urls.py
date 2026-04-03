from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile_view, name='profile'),

    path('myadmin/', views.myadmin, name='myadmin'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),

    path('addlaw/', views.addlaw, name='addlaw'),
    path('admin_viewlaw/', views.admin_viewlaw, name='admin_viewlaw'),
    path('admin_law_detailed_view/<int:law_id>/', views.admin_law_detailed_view, name='admin_law_detailed_view'),
    path('admin_user_profile/', views.admin_user_profile, name='admin_user_profile'),
    path('law_delete/<int:law_id>/', views.law_delete, name='law_delete'),
    path('law_update/<int:law_id>/', views.law_update, name='law_update'),

    path('categories/', views.view_categories, name='view_categories'),
    path('categories/<str:category>/', views.view_laws_by_category, name='view_laws_by_category'),
    path('adv_view_categories/', views.adv_view_categories, name='adv_view_categories'),
    path('adv_view_laws_by_category/<str:category>/', views.adv_view_laws_by_category, name='adv_view_laws_by_category'),


    

    path('addtemplate/', views.addtemplate, name='addtemplate'),
    path('templates/', views.admin_template_list, name='admin_template_list'),

    path('add_legal_office/', views.add_legal_office, name='add_legal_office'),
    path('admin_view_legal_office/', views.admin_view_legal_office, name='admin_view_legal_office'),
    path('admin_legal_office_detailed_view/<int:office_id>/', views.admin_legal_office_detailed_view, name='admin_legal_office_detailed_view'),
    path('legal_office_delete/<int:office_id>/', views.legal_office_delete, name='legal_office_delete'),
    path('legal_office_update/<int:office_id>/', views.legal_office_update, name='legal_office_update'),

    path('legal_office_list/', views.legal_office_list, name='legal_office_list'),
    path('legal_office_detail/<int:pk>/', views.legal_office_detail, name='legal_office_detail'),

    path('adv_legal_office_list/', views.adv_legal_office_list, name='adv_legal_office_list'),
    path('adv_legal_office_detail/<int:pk>/', views.adv_legal_office_detail, name='adv_legal_office_detail'),

    path('admin/challan/<int:transaction_id>/', views.admin_challan_detail, name='admin_challan_detail'),


    path("challan/form/", views.challan_form, name="challan_form"),
    path('challan/create-payment/', views.create_challan_payment, name='create_payment'),
    path('challan/paymenthandler/', views.challan_paymenthandler, name='challan_paymenthandler'),
    path('challan/success/', views.challan_success, name='challan_success'),
    path('challan/failed/', views.challan_failed, name='challan_failed'),




   

    path('add-awareness/', views.add_awareness_content, name='add_awareness'),




    path('template_delete/<int:template_id>/', views.template_delete, name='template_delete'),
    path('template_update/<int:template_id>/', views.template_update, name='template_update'),

    path('templist/', views.template_list, name='template_list'),
    path('adv_templist/', views.adv_template_list, name='adv_template_list'),
    path('filltemplate/<int:template_id>/', views.fill_template, name='fill_template'),
    path('adv_filltemplate/<int:template_id>/', views.adv_fill_template, name='adv_fill_template'),


    # path("templates/", views.template_list, name="template_list"),
    path("templates/fill/<int:template_id>/", views.fill_template, name="fill_template"),

    path('admin_template_detailed_view/<int:template_id>/', views.admin_template_detailed_view, name='admin_template_detailed_view'),

    path('advocates/', views.advocates, name='advocates'),
    path('advocate_home/', views.advocate_home, name='advocate_home'),
    path('advocate_register/', views.advocate_register, name='advocate_register'),

    # Custom admin advocate verification
    path("custom-admin/pending-advocates/", views.pending_advocates, name="pending_advocates"),
    path("custom-admin/approve-advocate/<int:advocate_id>/", views.approve_advocate, name="approve_advocate"),

    # ⭐ NEW LINE ADDED (Verified Advocates List)
    path("custom-admin/verified-advocates/", views.verified_advocates, name="verified_advocates"),
    path("custom-admin/delete-advocate/<int:advocate_id>/", views.delete_advocate, name="delete_advocate"),

    path('advocate_login/', views.advocate_login, name='advocate_login'),
    path('advocate_profile_view/', views.advocate_profile_view, name='advocate_profile_view'),
    path(
    'advocate/logout/',
    views.advocate_logout,
    name='advocate_logout'
),

path(
    'my-appointments/',
    views.user_appointments,
    name='user_appointments'
),



    # user feedback for advocates
    path("advocate/<int:id>/feedback/", views.send_feedback, name="send_feedback"),
    path('book-appointment/<int:advocate_id>/',views.book_appointment,name='book_appointment'),

    path(
        'advocate/appointments/',
        views.advocate_appointments,
        name='advocate_appointments'
    ),

    # ✅ Approve appointment
    path(
        'appointment/approve/<int:appointment_id>/',
        views.approve_appointment,
        name='approve_appointment'
    ),

    # ❌ Reject appointment
    path(
        'appointment/reject/<int:appointment_id>/',
        views.reject_appointment,
        name='reject_appointment'
    ),



    path('advocate/<int:id>/', views.advocate_detail, name='advocate_detail'),

    path('admin_advocate_profile/', views.admin_advocate_profile, name='admin_advocate_profile'),

    path("admin_challan_view/", views.admin_challan_view, name="admin_challan_view"),


    path('list/', views.law_list, name='law_list'),
    path('law/<int:pk>/', views.law_detail, name='law_detail'),
    path('law/<int:pk>/download/', views.download_law, name='download_law'),
    path('chat_view', views.chat_view, name='chat_view'),
    path('api/chat/', views.chat_api, name='chat_api'),
    path('chat/download/', views.download_chat, name='download_chat'),
   

    path('analyze-document/', views.legal_document_analysis, name='legal_document_analysis'),
    path("send-sos/", views.send_sos, name="send_sos"),
    path('admin_sos_alerts/', views.admin_sos_alerts, name='admin_sos_alerts'),


]
