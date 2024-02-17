from django.db import models
import uuid
# Create your models here.

STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)

class Resume(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name =  models.CharField(max_length = 50)
    dob = models.DateField(auto_now_add = False, auto_now = False)
    gender = models.CharField(max_length = 20)
    locality = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    pincode = models.PositiveIntegerField()
    state = models.CharField(choices = STATE_CHOICES, max_length = 30)
    mobile_no = models.CharField(max_length = 10)
    email = models.EmailField()
    job_location = models.CharField(max_length = 100)
    profile_img = models.ImageField(upload_to='profile_images')
    resume_file = models.FileField(upload_to='resume_files')

    def __str__(self) :
        return self.name


