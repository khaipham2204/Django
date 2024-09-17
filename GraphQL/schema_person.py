from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Person

class PersonNode(DjangoObjectType):
  '''
  Relay with Graphene-Django gives us some additional features:
  - Pagination and slicing.
  - An abstract id value which contains enough info for the server to know its type and its id.
  ...
  
    class Meta:
        model = Person
        filter_fields = {
            'full_name': ['exact', 'icontains', 'istartswith'],
            'address': ['exact', 'icontains'],
        }

        interfaces = (relay.Node, )
        
class Query(ObjectType):
    person = relay.Node.Field(PersonNode)
    all_persons = DjangoFilterConnectionField(PersonNode) 
