

from django.db import models


class UserData(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    language = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname
    


class Law(models.Model):
    
    law_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    section_no = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    sourcelink = models.URLField(blank=True, null=True)
    punishment = models.TextField(null=True, blank=True)
    bailable_status = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. Bailable or Non-Bailable")
    cognizable_status = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. Cognizable or Non-Cognizable")
    triable_by = models.CharField(max_length=200, blank=True, null=True, help_text="e.g. Magistrate of First Class")

    

    def __str__(self):
        # AutoField is an int; __str__ must return a string.
        # Prefer to show a readable title in admin.
        if self.title:
            return f"{self.title} ({self.section_no})" if self.section_no else self.title
        return str(self.law_id)






class LegalTemplate(models.Model):
    template_id = models.AutoField(primary_key=True)
    template_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    template_content = models.TextField()  # template body with placeholders
    uploaded_file = models.FileField(upload_to='legal_templates/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.template_name
    



# OPTIONAL: If advocate uploads proof (bar council ID)
    # verification_document = models.FileField(upload_to="advocate_docs/", null=True, blank=True)

class Advocate(models.Model):
    advocate_id = models.AutoField(primary_key=True)
    advocate_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    experience_years = models.IntegerField()
    location = models.CharField(max_length=255)
    availability_status = models.BooleanField(default=True)
    state_bar_council = models.CharField(max_length=255, null=True, blank=True)
    enrollment_number = models.CharField(max_length=100, null=True, blank=True)
    bar_council_idcard=models.FileField(upload_to='advocate_idcards/', blank=True, null=True)
    image = models.ImageField(upload_to='advocates/', blank=True, null=True)

    # NEW FIELD TO STORE MULTIPLE QUALIFICATIONS
    qualification = models.CharField(max_length=500, blank=True)

    # ⭐ NEW FIELDS FOR ADMIN VERIFICATION ⭐
    is_verified = models.BooleanField(default=False)  # Admin approval status
    verified_at = models.DateTimeField(null=True, blank=True)  # Timestamp when approved

    

    def __str__(self):
        return self.advocate_name
    




class Feedback(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    advocate = models.ForeignKey(Advocate, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 5+1)])  # 1–5 stars
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.fullname} → {self.advocate.advocate_name}"




    
class Payment(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserData, on_delete=models.CASCADE)
    challan_no = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.transaction_id} by {self.user_id.fullname}"

class Awareness_content(models.Model):
    content_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    link = models.URLField()
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class legal_office(models.Model):
    office_id = models.AutoField(primary_key=True)
    office_name = models.CharField(max_length=255)
    address = models.TextField()
    location = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    offences_handled = models.TextField()
    working_hours = models.CharField(max_length=100)

    def __str__(self):
        return self.office_name
    

class Challan(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE, null=True, blank=True)
    challan_no = models.AutoField(primary_key=True)
    offence_type = models.CharField(max_length=255)
    offence_location = models.CharField(max_length=255)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    status = models.BooleanField(default=False)  # paid or not

    def __str__(self):
        return f"{self.challan_no} - {self.user.username}"
    






class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    advocate = models.ForeignKey(Advocate, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    status = models.CharField(
        max_length=50,
        choices=[
            ('Pending', 'Pending'),
            ('Scheduled', 'Scheduled'),

            ('Completed', 'Completed'),
            ('Cancelled', 'Cancelled')
        ],
        default='Pending'
    )

    def __str__(self):
        return f"Appointment {self.appointment_id} - {self.user.fullname} with {self.advocate.advocate_name}"



class LegalDocument(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    file = models.FileField(upload_to='legal_docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    ai_summary = models.TextField(blank=True, null=True)

class SOS(models.Model):
    sos_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SOS Alert from {self.user.fullname}"

class AIChatCache(models.Model):
    query = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query[:50]

class AIDocumentCache(models.Model):
    text_hash = models.CharField(max_length=64, unique=True)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text_hash
