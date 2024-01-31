import graphene
from app.models import Contact, Profile
from .schema import ContactType,ProfileType,Query


# mutation class is used for creating a data
class ContactMutations(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        phoneNumber = graphene.String()
    contact = graphene.Field(ContactType)
    message = graphene.String()
    @classmethod
    def mutate(cls, root, info, name, phoneNumber):
        contact = Contact(name=name, phoneNumber=phoneNumber)
        contact.save()
        return ContactMutations(contact=contact, message="Contact successfully created")

class UpdateContact(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        phoneNumber = graphene.String()
    contact = graphene.Field(ContactType)
    message = graphene.String()
    @classmethod
    def mutate(cls, root, info, name, phoneNumber, id):
        contact = Contact(name=name, phoneNumber=phoneNumber)
        # contact.save()

        get_contact = Contact.objects.get(id=id)
        get_contact.name = name
        get_contact.phoneNumber = phoneNumber
        get_contact.save()
        return UpdateContact(message="Updated successfully!!")
        
class ContactDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    contact = graphene.Field(ContactType)
    message = graphene.String()
    @classmethod
    def mutate(cls, root, info, id):
        contact = Contact.objects.get(id=id)
        contact.delete()
        return ContactDelete(message = "Deleted successfully!!")


class ProfileMutations(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        phoneNumber = graphene.String()
        address = graphene.String()
        sex = graphene.String()
    profile = graphene.Field(ProfileType)
    message = graphene.String()
    @classmethod
    def mutate(cls, root, info, name, address, phoneNumber, sex):
        profile = Profile(name=name, phoneNumber=phoneNumber, address=address, sex=sex)
        profile.save()
        return ProfileMutations(message="Profile successfully created")
    
class UpdateProfile(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        phoneNumber = graphene.String()
        address = graphene.String()
        sex = graphene.String()
    profile = graphene.Field(ProfileType)
    message = graphene.String()
    @classmethod
    def mutate(cls, root, info, name, phoneNumber, address, sex, id):
        profile = Profile(name=name, phoneNumber=phoneNumber, address=address, sex=sex)

        profile_data = Profile.objects.get(id=id)
        profile_data.name = name
        profile_data.phoneNumber = phoneNumber
        profile_data.address =address
        profile_data.sex = sex
        profile_data.save()
        
        return UpdateProfile(message = "Updated successfully")

class ProfileDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    profile = graphene.Field(ProfileType)
    message = graphene.String()
    @classmethod
    def mutate(cls,root, info, id):
        profile = Profile.objects.get(id=id)
        profile.delete()
        return ProfileDelete(message="Deleted successfully")

class Mutation(graphene.ObjectType):
    createContact = ContactMutations.Field()
    createProfile = ProfileMutations.Field()
    deleteContact = ContactDelete.Field()
    deleteProfile = ProfileDelete.Field()
    updateContact = UpdateContact.Field()
    updateProfile = UpdateProfile.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

