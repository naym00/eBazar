from distutils.command.upload import upload
from django.contrib.postgres.fields import ArrayField
from django.db import models
from mobile import static_data

class Mobile_Description(models.Model):
    brand = models.CharField('Mobile Brand', max_length=50, choices=static_data.MOBILE_BRADS, default=static_data.MOBILE_BRADS[0][0])
    release_date = models.DateField('Release Date')
    weight = models.CharField('Net Wight', max_length=20)
    dimensions = models.CharField('Dimensions', max_length=100)
    body_material = models.CharField('Body Material', max_length=100)
    sim = models.CharField('Sim', max_length=100)
    screen_size = models.CharField('Screen Size', max_length=100)
    resolution = models.CharField('Resolution', max_length=100)
    os = models.CharField('Operating System', max_length=100)
    chipset = models.CharField('Chipset', max_length=100)
    processor = models.CharField('Processor', max_length=100)
    front_camera = models.CharField('Front Camera', max_length=100)
    front_camera_video_recording = models.CharField('Front Camera Video Recording', max_length=100)
    back_camera = models.CharField('Back Camera', max_length=100)
    back_camera_video_recording = models.CharField('Back Camera Video Recording', max_length=100)
    usb_type = models.CharField('USB Type', max_length=100)
    otg = models.BooleanField('OTG')
    fingerprint = models.BooleanField('Fingerprint')
    face_lock = models.BooleanField('Face Lock')
    made_in = models.CharField('Made in', max_length=50)
    battery_capacity = models.CharField('Battery Capacity', max_length=100)
    water_resistance = models.BooleanField('Water Resistance')
    bluetooth = models.BooleanField('Bluetooth')
    fast_charging = models.CharField('Fast Charging', max_length=100) 
    sensors = ArrayField(models.CharField(max_length=200), blank=True)
    radio = ArrayField(models.CharField(max_length=200), blank=True)
    gps = ArrayField(models.CharField(max_length=200), blank=True)
    wlan = ArrayField(models.CharField(max_length=200), blank=True)
    network = ArrayField(models.CharField(max_length=200), blank=True)
    model = models.CharField('Model', max_length=100)

    def __str__(self):
        return self.brand + " " +self.model

class Mobile_Colors(models.Model):
    mobile_description = models.ForeignKey(Mobile_Description, on_delete=models.CASCADE, default=None, verbose_name='Select Mobile')
    color = models.CharField('Color', max_length=100)

    def __str__(self):
        return self.mobile_description.model + " " + self.color

class Mobile_Images(models.Model):
    mobile_colors = models.ForeignKey(Mobile_Colors, on_delete=models.CASCADE, default=None, verbose_name='Select Mobile')
    photo = models.ImageField('Image', upload_to = 'product\\mobile\\images')

    def __str__(self):
        return self.mobile_colors.mobile_description.model + " " + self.mobile_colors.color

class Mobile_Ram_Rom(models.Model):
    mobile_description = models.ForeignKey(Mobile_Description, on_delete=models.CASCADE, default=None, verbose_name='Select Mobile')
    price= models.IntegerField('Price')
    ram = models.CharField('RAM', max_length=100)
    rom = models.CharField('ROM', max_length=100)

    def __str__(self):
        return self.mobile_description.model + " " + self.ram + " " + self.rom