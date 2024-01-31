import pytest
from graphene.test import Client
from app.models import Contact, Profile
from graphql_tutorial.schema import schema

@pytest.fixture
def graphql_client():
    return Client(schema)

@pytest.mark.django_db
def test_list_contact(graphql_client):
    contact1 = Contact.objects.create(name="John Doe", phoneNumber="1234567890")
    contact2 = Contact.objects.create(name="Jane Doe", phoneNumber="9876543210")

    result = graphql_client.execute("""
        query{
            listContact{
                id
                name
                phoneNumber          
            }
        }
    """)
    print(f"result {result}")
    assert result['data']['listContact'] == [
        {
            'id': str(contact1.id), 'name': contact1.name, 
            'phoneNumber':contact1.phoneNumber
        },
        {
            'id': str(contact2.id), 'name': contact2.name,  
            'phoneNumber': contact2.phoneNumber
        }
    ]

@pytest.mark.django_db
def test_read_contact(graphql_client):
    contact = Contact.objects.create(name="John Doe", phoneNumber="9876543210")
    result = graphql_client.execute("""
        query ReadContact($id: Int!){
            readContact(id: $id){
                id
                name
                phoneNumber
            }
        }
    """, variable_values={'id': contact.id})
    assert result['data']['readContact'] == {
        'id': str(contact.id),
        'name': contact.name,
        'phoneNumber': contact.phoneNumber,
    }

@pytest.mark.django_db
def test_list_profile(graphql_client):
    profile1 = Profile.objects.create(
        name="John Doe", phoneNumber="9876543210", address="Test Address", sex="male"
        )
    profile2 = Profile.objects.create(
        name="Jane Doe", phoneNumber="1234567890", address="test Address", sex="female"
        )

    result = graphql_client.execute("""
        query{
            listProfile{
                    id
                    name
                    phoneNumber
                    address                
                    sex
            }
        }
    """)
    print(f"result{result}")
    # assert result['data']['listProfile'] == [
    expected_data =[
        {
            'id': str(profile1.id), 'name': profile1.name, 'phoneNumber': profile1.phoneNumber,
            'address': profile1.address, 'sex': profile1.sex.upper()
        },
        {
            'id': str(profile2.id), 'name': profile2.name, 'phoneNumber': profile2.phoneNumber,
            'address': profile2.address, 'sex': profile2.sex.upper()
        }
    ]
    assert result['data']['listProfile'] == expected_data

@pytest.mark.django_db
def test_read_profile(graphql_client):
    profile = Profile.objects.create(
        name="John Doe", phoneNumber="9876543210", address="Test Address", sex="male"
        )
    result = graphql_client.execute("""
        query ReadProfile($id: Int!){
            readProfile(id: $id){
                id
                name
                phoneNumber
                address
                sex
            }
        }
    """, variable_values={'id': profile.id})
    assert result['data']['readProfile'] == {
        'id': str(profile.id),
        'name': profile.name,
        'phoneNumber': profile.phoneNumber,
        'address': profile.address,
        'sex': profile.sex.upper()
    }
