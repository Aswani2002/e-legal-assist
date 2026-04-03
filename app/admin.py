from django.contrib import admin
from .models import UserData, Law, LegalTemplate, Advocate, Payment, Awareness_content, Feedback, legal_office, Challan, Appointment, LegalDocument


# Register UserData with an admin class
@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'language', 'location', 'contact_no')
    search_fields = ('fullname', 'email')
    list_filter = ('language',)


# Register Law model with a simple admin configuration
@admin.register(Law)
class LawAdmin(admin.ModelAdmin):
    list_display = ('law_id', 'category', 'section_no', 'title')
    search_fields = ('title', 'category', 'section_no')
    list_filter = ('category',)


@admin.register(LegalTemplate)
class LegalTemplateAdmin(admin.ModelAdmin):
    list_display = ('template_id', 'template_name', 'category', 'created_at')
    search_fields = ('template_name', 'category')
    list_filter = ('category', 'created_at')

@admin.register(Advocate)
class AdvocateAdmin(admin.ModelAdmin):
    list_display = (
        'advocate_id',
        'advocate_name',
        'specialization',
        'qualification',
        'email',
        'experience_years',
        'location',
        'availability_status',
        'image'
    )

    search_fields = ('advocate_name', 'specialization','qualification', 'location', 'email')
    
    list_filter = ('specialization','qualification', 'location', 'availability_status')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'user_id', 'amount', 'payment_date', 'status')
    search_fields = ('user_id__fullname', 'challan_no')
    list_filter = ('status', 'payment_date')



@admin.register(Awareness_content)
class AwarenessContentAdmin(admin.ModelAdmin):
    list_display = ('content_id', 'title', 'type', 'category', 'upload_date')
    search_fields = ('title', 'type', 'category')
    list_filter = ('type', 'category', 'upload_date')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'advocate', 'rating', 'created_at')
    search_fields = ('user__fullname', 'advocate__advocate_name')
    list_filter = ('rating', 'created_at')


@admin.register(legal_office)
class LegalOfficeAdmin(admin.ModelAdmin):
    list_display = ('office_id', 'office_name', 'location', 'contact_no', 'email')
    search_fields = ('office_name', 'location', 'email')
    list_filter = ('location',)


class ChallanAdmin(admin.ModelAdmin):
    list_display = (
        'challan_no',
        'user',              # 👈 NEW
        'offence_type',
        'offence_location',
        'issue_date',
        'due_date',
        'fine_amount',
        'status',
    )

    list_filter = (
        'status',
        'issue_date',
        'due_date',
        'user',              # 👈 Filter by user
    )

    search_fields = (
        'challan_no',
        'offence_type',
        'offence_location',
        'description',
        'user__username',    # 👈 Search by username
        'user__email',       # 👈 Search by user email
    )

admin.site.register(Challan, ChallanAdmin)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'appointment_id',
        'user',
        'advocate',
        'appointment_date',
        'status',
    )

    list_filter = (
        'status',
        'appointment_date',
    )

    search_fields = (
        'user__fullname',
        'advocate__advocate_name',
    )

@admin.register(LegalDocument)
class LegalDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'file', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('user__email',)
    readonly_fields = ('uploaded_at', 'ai_summary')