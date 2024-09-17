import graphene
from . import schema_contact, schema_person

class Query(schema_contact.Query, schema_person.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(schema_contact.Mutation, graphene.ObjectType):
    # This class will inherit from multiple Mutation
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
