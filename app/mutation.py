import graphene
from app.models import Contact, Profile
from .schema import ContactType,ProfileType,Query


# mutation class is used for creating a data
class ContactMutations(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        phone_number = graphene.String()
    Contact = graphene.Field(ContactType)
    message = graphene.String()
    @classmethod
    def mutate(cls, root, info, name, phone_number):
        contact = Contact(name=name, phone_number=phone_number)
        contact.save()
        return ContactMutations(contact=contact, message="Contact successfully created")

class UpdateContact(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        phone_number = graphene.String()
    contact = graphene.Field(ContactType)
    message = graphene.String()
    @classmethod
    def mutate(cls, root, info, name, phone_number, id):
        contact = Contact(name=name, phone_number=phone_number)
        # contact.save()

        get_contact = Contact.objects.get(id=id)
        get_contact.name = name
        get_contact.phone_number = phone_number
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
        phone_number = graphene.String()
        address = graphene.String()
        sex = graphene.String()
    Profile = graphene.Field(ProfileType)
    message = graphene.String()
    @classmethod
    def mutate(cls, root, info, name, address, phone_number, sex):
        profile = Profile(name=name, phone_number=phone_number, address=address, sex=sex)
        profile.save()
        return ProfileMutations(message="Profile successfully created")
    
class UpdateProfile(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        phone_number = graphene.String()
        address = graphene.String()
        sex = graphene.String()
    profile = graphene.Field(ProfileType)
    message = graphene.String()
    @classmethod
    def mutate(cls, root, info, name, phone_number, address, sex, id):
        profile = Profile(name=name, phone_number=phone_number, address=address, sex=sex)

        profile_data = Profile.objects.get(id=id)
        profile_data.name = name
        profile_data.phone_number = phone_number
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
    create_contact = ContactMutations.Field()
    create_profile = ProfileMutations.Field()
    delete_contact = ContactDelete.Field()
    delete_profile = ProfileDelete.Field()
    update_contact = UpdateContact.Field()
    update_profile = UpdateProfile.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)