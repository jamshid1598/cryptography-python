from django.db import models
from django.forms import Textarea

# Create your models here.





class CryptoKey(models.Model):
    private_key = models.TextField()
    public_key = models.TextField()
    
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ['id', 'created_at']
        verbose_name = 'RSA encryption keys'
        verbose_name_plural = 'RSA encryption keys'
        
    def __str__(self):
        return "%s"%self.id

    
class CryptoMessage(models.Model):
    message = models.TextField()
    encmessage = models.TextField(blank=True, null=True)
    
    public_key = models.TextField(blank=True, null=True)
    
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ['id', 'created_at']
        verbose_name = 'Message'
        verbose_name_plural = 'Message'
        
    def __str__(self):
        return "%s"%self.id