from rest_framework import serializers
from .models import *
import phonenumbers, re


class LibrarySerializer(serializers.ModelSerializer):
    contact_email = serializers.EmailField(required=True)

    class Meta:
        model = Library
        fields = '__all__'

    def validate_phone_number(self, value):
        try:
            parsed = phonenumbers.parse(value, None)
        except phonenumbers.NumberParseException:
            try:
                parsed = phonenumbers.parse(value, "IN")
            except phonenumbers.NumberParseException:
                raise serializers.ValidationError("Could not parse phone number.")

        if not phonenumbers.is_valid_number(parsed):
            raise serializers.ValidationError("Phone number is not valid.")
        formatted_number = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
        return formatted_number


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_isbn(self, value):
        isbn = value.replace('-', '').upper()
        if len(isbn) == 13 and isbn.isdigit():
            total = sum((int(x) * (1 if i % 2 == 0 else 3)) for i, x in enumerate(isbn))
            if total % 10 != 0:
                raise serializers.ValidationError('Invalid ISBN-13 checksum')
            return isbn
        elif len(isbn) == 10 and re.match(r'^\d{9}[\dXx]$', isbn):
            total = sum((10 - i) * (10 if x.upper() == 'X' else int(x)) for i, x in enumerate(isbn))
            if total % 11 != 0:
                raise serializers.ValidationError('Invalid ISBN-10 checksum')
            return isbn
        else:
            raise serializers.ValidationError('ISBN must be 10 or 13 digits long')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    def validate(self, data):
        if 'first_name' in data:
            data['first_name'] = ' '.join(data['first_name'].strip().split()).title()
        if 'last_name' in data:
            data['last_name'] = ' '.join(data['last_name'].strip().split()).title()
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    has_overdue = serializers.SerializerMethodField()
    contact_email = serializers.EmailField(required=True)

    class Meta:
        model = Member
        fields = '__all__'

    def get_has_overdue(self, obj):
        return obj.has_overdue_books()

    def validate_phone_number(self, value):
        try:
            parsed = phonenumbers.parse(value, None)
        except phonenumbers.NumberParseException:
            try:
                parsed = phonenumbers.parse(value, "IN")
            except phonenumbers.NumberParseException:
                raise serializers.ValidationError("Could not parse phone number.")

        if not phonenumbers.is_valid_number(parsed):
            raise serializers.ValidationError("Phone number is not valid.")
        formatted_number = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
        return formatted_number


class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = '__all__'

    def validate(self, data):
        borrow_date = data.get('borrow_date')
        return_date = data.get('return_date')
        late_fee = data.get('late_fee')

        if return_date and borrow_date and return_date < borrow_date:
            raise serializers.ValidationError("Return date cannot be before borrow date.")

        if late_fee is not None and late_fee < 0:
            raise serializers.ValidationError("Late fee cannot be negative.")

        return data


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = ['book', 'author']


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ['book', 'category']
