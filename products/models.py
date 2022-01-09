from django.db import models

class Menu(models.Model):
	
	name = models.CharField(max_length=20)
	
	
	class Meta:
		db_table = 'menus'

class Category(models.Model):
	
	name = models.CharField(max_length=20)
	
	menu = models.ForeignKey('Menu', on_delete=models.CASCADE,null=True)	

	
	class Meta:
	
		db_table = 'categories'


class Drink(models.Model):
	
	category = models.ForeignKey('Category', on_delete=models.CASCADE,null=True)	
	korean_name = models.CharField(max_length=100)

	foreign_name = models.CharField(max_length=100)
	

	class Meta:

		db_table = 'drinks'

class Nutrition(models.Model):

	serving_size_kcal = models.IntegerField(blank=False)
	
	sodium = models.IntegerField(blank=False)

	saturated_fat = models.IntegerField(blank=False)

	caffeine = models.IntegerField(blank=False)

	sugars = models.IntegerField(blank=False)

	protein = models.IntegerField(blank=False)
	
	drink = models.ForeignKey('Drink', on_delete=models.CASCADE,null=True)
		
	
	class Meta:
	
		db_table = 'nutritions'

class Allergy(models.Model):
	
	name = models.CharField(max_length=100)
	
	drink = models.ForeignKey('Drink', on_delete=models.CASCADE,null=True)	

	
	class Meta:
	
		db_table = 'allergies'

class Image(models.Model):

	image_url = models.CharField(max_length=500)
	
	drink = models.ForeignKey('Drink', on_delete=models.CASCADE,null=True)	
	
	
	class Meta:

		db_table = 'images'
