from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

	def _create_user(self, username, phonenumber, email, password, is_staff, is_superuser, **extra_fields):
		if not username:
			raise ValueError('Username must be required')
		if not phonenumber:
			raise ValueError('Phone number must be required')
		email = self.normalize_email(email)
		user = self.model(
			username=username,
			phonenumber=phonenumber,
			email=email,
			is_active=True,
			is_staff=is_staff, 
			is_superuser=is_superuser, 
			**extra_fields
		)
	
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, username, phonenumber, email, password, **extra_fields):
		return self._create_user(username, phonenumber, email, password, False, False, **extra_fields)

	def create_superuser(self, username, phonenumber, email, password, **extra_fields):
		return self._create_user(username, phonenumber, email, password, True, True, **extra_fields)