import pytest
from graphene.test import Client
from django.contrib.auth.models import User
from graphql_tutorial.schema import schema
from ..models import Contact, Profile

@pytest.fixture
def graphql_client():
    return Client(schema)

@pytest.mark.django_db
def test_create_contact_mutation(graphql_client):
    mutation = '''
    mutation {
        createContact(name: "John Doe", phoneNumber: "1234567890") {
            contact {
                id
                name
                phoneNumber
            }
            message
        }
    }
    '''
    result = graphql_client.execute(mutation)
    assert "errors" not in result
    assert result["data"]["createContact"]["message"] == "Contact successfully created"

    contact_id = result["data"]["createContact"]["contact"]["id"]
    assert Contact.objects.filter(id=contact_id).exists()

@pytest.mark.django_db
def test_update_contact_mutation(graphql_client):
    existing_contact = Contact.objects.create(name="Existing Contact", phoneNumber="9876543210")

    mutation = f'''
    mutation {{
        updateContact(id: "{existing_contact.id}", name: "Updated Contact", phoneNumber: "5555555555") {{
            message
        }}
    }}
    '''
    result = graphql_client.execute(mutation)
    assert "errors" not in result
    assert result["data"]["updateContact"]["message"] == "Updated successfully!!"

    updated_contact = Contact.objects.get(id=existing_contact.id)
    assert updated_contact.name == "Updated Contact"
    assert updated_contact.phoneNumber == "5555555555"

@pytest.mark.django_db
def test_delete_contact_mutation(graphql_client):
    existing_contact = Contact.objects.create(name="Existing Contact", phoneNumber="9876543210")

    mutation = f'''
    mutation {{
        deleteContact(id: "{existing_contact.id}") {{
            message
        }}
    }}
    '''
    result = graphql_client.execute(mutation)
    assert "errors" not in result
    assert result["data"]["deleteContact"]["message"] == "Deleted successfully!!"
    assert not Contact.objects.filter(id=existing_contact.id).exists()

@pytest.mark.django_db
def test_create_profile_mutation(graphql_client):
    mutation = '''
    mutation {
        createProfile(
            name: "John Doe",
            phoneNumber: "1234567890",
            address: "Test Address", 
            sex: "male"
        ) {
            message
        }
    }
    '''

    result = graphql_client.execute(mutation)
    assert "errors" not in result
    assert result["data"]["createProfile"]["message"] == "Profile successfully created"

@pytest.mark.django_db
def test_update_profile_mutation(graphql_client):
    existing_profile = Profile.objects.create(
        name="Existing Profile",
        phoneNumber="987654321",
        address="456 Second St",
        sex="Female"
    )

    existing_profile1 = Profile.objects.create(
        name="John Doe",
        phoneNumber="8546422561",
        address="Test address",
        sex="male"
    )

    mutation = f'''
        mutation{{
            updateProfile(
                id:{existing_profile.id},
                name:"Updated Profile",
                phoneNumber: "11231231251",
                address: "Test Address",
                sex: "Male"
            ){{
                message
            }}
        }}
    '''
    result = graphql_client.execute(mutation)
    assert "errors" not in result
    assert result["data"]["updateProfile"]["message"] == "Updated successfully"

@pytest.mark.django_db
def test_delete_profile_mutation(graphql_client):
    existing_profile = Profile.objects.create(
        name="John Doe",
        phoneNumber="9876543210",
        address="Vatigan city",
        sex="male"
    )
    existing_profile1 = Profile.objects.create(
        name = "Hello",
        phoneNumber = "123456789",
        address = "test address",
        sex = "female"
    )
    mutation = f'''
        mutation{{
            deleteProfile(id:{existing_profile.id}){{
                message
            }}
        }}
    '''
    mutation1 = f'''
        mutation{{
            deleteProfile(id: {existing_profile1.id}){{
                message
            }}
        }}
    '''

    result = graphql_client.execute(mutation)
    assert "errors" not in result
    assert result["data"]["deleteProfile"]["message"] == "Deleted successfully"

    result1 = graphql_client.execute(mutation1)
    assert "errors" not in result1
    assert result1["data"]["deleteProfile"]["message"] == "Deleted successfully"