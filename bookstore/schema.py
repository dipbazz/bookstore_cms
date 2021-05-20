import graphene
from graphene_django import DjangoObjectType

from bookstore.models import Category, Book


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class Query(graphene.AbstractType):
    books = graphene.List(BookType)
    categories = graphene.List(CategoryType)

    def resolve_books(root, info):
        return Book.objects.all()

    def resolve_categories(root, info):
        return Category.objects.all()
