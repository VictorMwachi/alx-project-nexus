from django.db import models
import uuid

# Create your models here.
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ProductDepartment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    department = models.ForeignKey(ProductDepartment, related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class ProductSubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(ProductCategory, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    description = models.TextField()
    product_details = models.TextField(blank=True, null=True)
    specifications = models.JSONField(blank=True, null=True)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, related_name='products', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(ProductSubCategory, related_name='products', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name} - {self.name}"
    
class ProductImage(models.Model):
    """
    Represents an image associated with a product.
    Fields:
        id (AutoField): Primary key for the image.
        image_uuid (UUIDField): Unique identifier for the image, generated automatically.
        product (ForeignKey): Reference to the related Product instance. Deleting the product deletes its images.
        image (ImageField): The actual image file, uploaded to 'product_images/' directory.
        image_name (CharField): Unique name for the image, defaults to a generated UUID.
    Methods:
        __str__(): Returns a string representation of the image, including its name and associated product's name.
    """
    id = models.AutoField(primary_key=True)
    image_uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(
        upload_to='product_images/',
        help_text='Upload a JPEG or PNG image (max size: 5MB).'
    )
    
    def __str__(self):
        return f"Image {self.image_uuid} for {self.product.name} and variant {self.product_variant.name if self.product_variant else 'N/A'} "
