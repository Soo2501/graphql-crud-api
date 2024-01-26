import graphene 
from graphene_django import DjangoObjectType
from app.models import Contact, Profile


class ContactType(DjangoObjectType):
    class Meta:
        model = Contact
        field = ("id", "name", "phone_number")

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ("id", "name", "phone_number", "address", "sex")

class Query(graphene.ObjectType):
    list_contact = graphene.List(ContactType)
    read_contact = graphene.Field(ContactType, id=graphene.Int())
    
    list_profile = graphene.List(ProfileType)
    read_profile = graphene.Field(ProfileType, id=graphene.Int())

    def resolve_list_contact(root, info):
        return Contact.objects.all()
    
    def resolve_read_contact(root, info, id):
        return Contact.objects.get(id=id)

    def resolve_list_profile(root, info):
        return Profile.objects.all()
  
    def resolve_read_profile(root, info, id):
        return Profile.objects.get(id=id)
        
# schema = graphene.Schema(query=Query)


