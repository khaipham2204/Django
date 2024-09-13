import graphene
from graphene_django import DjangoObjectType
from .models import Contact

# Types:
class ContactType(DjangoObjectType):
    # Describe the data that is to be formatted into GraphQL fields
    class Meta:
        model = Contact
        fields = ("id", "name", "phone_number")
        
#  Input Type for Contact: POST, PUT, DELETE methods
class ContactInput(graphene.InputObjectType):
    id = graphene.Int()
    name = graphene.String()
    phone_number = graphene.String()
      
# Query:
class Query(graphene.ObjectType):
    # List all contacts
    list_contact = graphene.List(ContactType)
    
    # Retrieve a single contact by ID
    read_contact = graphene.Field(ContactType, id=graphene.Int())
    
    # Resolve hook:
    def resolve_list_contact(root, info):
        return Contact.objects.all()

    def resolve_read_contact(root, info, id):
        try:
            return Contact.objects.get(id=id)
        except Contact.DoesNotExist:
            return None

class CreateContactMutation(graphene.Mutation):
    
    class Arguments:
        input = graphene.Argument(ContactInput)
        
    # Define what the mutation returns
    contact = graphene.Field(ContactType)
    
    @classmethod
    def mutate(cls, root, info, input):
        # Create new contact
        contact = Contact.objects.create(
            name=input.name,
            phone_number=input.phone_number
        )
        return CreateContactMutation(contact=contact)
 
 
class UpdateContactMutation(graphene.Mutation):
    class Arguments:
        input = graphene.Argument(ContactInput)

    contact = graphene.Field(ContactType)
    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, input):
        updated_rows = Contact.objects.filter(id=input.id).update(
            name=input.name,
            phone_number=input.phone_number
        )
        if updated_rows:
            contact = Contact.objects.get(id=input.id)
            return UpdateContactMutation(contact=contact, message="Contact updated successfully")
        else:
            return UpdateContactMutation(contact=None, message="Contact with given ID does not exist")
    
class DeleteContactMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    message = graphene.String()
    
    @classmethod
    def mutate(cls, root, info, id):
        try:
            # Try to retrieve the contact by ID
            contact = Contact.objects.get(id=id)
            
            # Delete the contact
            contact.delete()
            return DeleteContactMutation(success=True, message="Contact deleted successfully")
        except Contact.DoesNotExist:
            # Return success=False if the contact doesn't exist
            return DeleteContactMutation(success=False, message="Contact with given ID does not exist")

# Mutation:
class Mutation(graphene.ObjectType):
    create_contact = CreateContactMutation.Field()
    update_contact = UpdateContactMutation.Field()
    delete_contact = DeleteContactMutation.Field()

# Schema:
schema = graphene.Schema(query=Query, mutation=Mutation)
