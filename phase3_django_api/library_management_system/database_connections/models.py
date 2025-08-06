# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authors(models.Model):
    author_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'authors'


class Bookauthor(models.Model):
    pk = models.CompositePrimaryKey('book_id', 'author_id')
    book = models.ForeignKey('Books', models.DO_NOTHING)
    author = models.ForeignKey(Authors, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bookauthor'


class Bookcategory(models.Model):
    pk = models.CompositePrimaryKey('book_id', 'category_id')
    book = models.ForeignKey('Books', models.DO_NOTHING)
    category = models.ForeignKey('Categories', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bookcategory'


class Books(models.Model):
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    isbn = models.CharField(unique=True, max_length=20, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    total_copies = models.IntegerField(blank=True, null=True)
    available_copies = models.IntegerField(blank=True, null=True)
    library = models.ForeignKey('Libraries', models.DO_NOTHING, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'books'


class Borrowing(models.Model):
    borrowing_id = models.IntegerField(primary_key=True)
    member = models.ForeignKey('Members', models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(Books, models.DO_NOTHING, blank=True, null=True)
    borrow_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    late_fee = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'borrowing'


class Categories(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    descriptions = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categories'



class Libraries(models.Model):
    library_id = models.IntegerField(primary_key=True)
    library_name = models.CharField(max_length=50)
    campus_location = models.CharField(max_length=50, blank=True, null=True)
    contact_email = models.CharField(unique=True, max_length=50, blank=True, null=True)
    phone_number = models.CharField(unique=True, max_length=15, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'libraries'


class Members(models.Model):
    member_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=50, blank=True, null=True)
    phone_number = models.CharField(unique=True, max_length=15, blank=True, null=True)
    member_type = models.CharField(max_length=20, blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'members'


class Reviews(models.Model):
    review_id = models.IntegerField(primary_key=True)
    member = models.ForeignKey(Members, models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(Books, models.DO_NOTHING, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    review_date = models.DateField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reviews'
        unique_together = (('member', 'book'),)
