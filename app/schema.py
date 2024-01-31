import graphene 
from graphene_django import DjangoObjectType
from app.models import Contact, Profile


class ContactType(DjangoObjectType):
    class Meta:
        model = Contact
        field = ("id", "name", "phoneNumber")

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ("id", "name", "phoneNumber", "address", "sex")

class Query(graphene.ObjectType):
    listContact = graphene.List(ContactType)
    readContact = graphene.Field(ContactType, id=graphene.Int())
    
    listProfile = graphene.List(ProfileType)
    readProfile = graphene.Field(ProfileType, id=graphene.Int())

    def resolve_listContact(root, info):
        return Contact.objects.all()
    
    def resolve_readContact(root, info, id):
        return Contact.objects.get(id=id)

    def resolve_listProfile(root, info):
        return Profile.objects.all()
  
    def resolve_readProfile(root, info, id):
        return Profile.objects.get(id=id)
        
# schema = graphene.Schema(query=Query)


