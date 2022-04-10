from django.db import models


# Create your models here.

class CryptoKey(models.Model):
    name = models.CharField(max_length=400, blank=True, null=True)
    private_key = models.TextField()
    public_key = models.TextField()
    
    private_key_file = models.FileField(upload_to='keys/privateKey/', blank=True, null=True)
    public_key_file = models.FileField(upload_to='keys/publicKeys/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['id', 'name', 'created_at']
        verbose_name = 'RSA encryption keys'
        verbose_name_plural = 'RSA encryption keys'
        
    def __str__(self):
        return "%s"%self.name
    
    @property
    def privateKeyUrl(self):
        try:
            return self.private_key_file.url
        except:
            return ''
    
    @property
    def publicKeyUrl(self):
        try:
            return self.public_key_file.url
        except:
            return ''
    
    
class CryptoMessage(models.Model):
    message = models.TextField()
    encmessage = models.TextField(blank=True, null=True)
    
    public_key = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['id', 'created_at']
        verbose_name = 'Message'
        verbose_name_plural = 'Message'
        
    def __str__(self):
        return "%s"%self.id