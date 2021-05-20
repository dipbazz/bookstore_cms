import graphene

import bookstore.schema

class Query(bookstore.schema.Query, graphene.ObjectType):
    pass


class Mutation(bookstore.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
