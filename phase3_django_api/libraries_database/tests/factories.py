import factory
from faker import Faker
from libraries_database import models

fake = Faker()


class LibraryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Library

    name = factory.Faker("company")
    location = factory.Faker("city")


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Faker("word")


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Author

    name = factory.Faker("name")
    birth_date = factory.Faker("date_of_birth")
    nationality = factory.Faker("country")


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Book

    title = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("paragraph")
    total_copies = 5
    available_copies = 5
    library = factory.SubFactory(LibraryFactory)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for category in extracted:
                self.categories.add(category)

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for author in extracted:
                self.authors.add(author)


class MemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Member

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.LazyAttribute(lambda _: fake.unique.email())


class BorrowingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Borrowing

    member = factory.SubFactory(MemberFactory)
    book = factory.SubFactory(BookFactory)
    borrow_date = factory.Faker("date_this_year")
    due_date = factory.Faker("date_this_year")
    return_date = None
    late_fee = 0
