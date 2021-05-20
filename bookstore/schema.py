import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoFormMutation

from bookstore.models import Category, Book
from bookstore.forms import BookForm

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
    book = graphene.Field(BookType, id=graphene.ID())
    categories = graphene.List(CategoryType)

    def resolve_books(root, info):
        return Book.objects.all()

    def resolve_book(root, info, id):
        return Book.objects.get(pk=id)

    def resolve_categories(root, info):
        return Category.objects.all()


class BookDeleteMutation(graphene.Mutation):
    ok = graphene.Boolean()
    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, id):
        book = Book.objects.get(pk=id)
        book.delete()
        return cls(ok=True)

class BookCreateMutation(DjangoFormMutation):
    class Meta:
        form_class = BookForm



class Mutation(graphene.ObjectType):
    remove_book = BookDeleteMutation.Field()
    create_book = BookCreateMutation.Field()
