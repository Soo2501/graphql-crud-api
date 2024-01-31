from django.test import TestCase
from app.models import Contact, Profile

class ContactTest(TestCase):
    def setUp(self):
        self.contact1 = Contact.objects.create(
            id = 1,
            name= "Test1",
            phoneNumber = "984521222"
        )
    def test_contact_model(self):
        self.assertEqual(self.contact1.name, 'Test1')
        self.assertEqual(self.contact1.phoneNumber, '984521222')

    def test_str_representation(self):
        self.assertEqual(str(self.contact1), "Test1 id: 1")

class ProfileTest(TestCase):
    def setUp(self):
        self.profile1 = Profile.objects.create(
            name = "Test Test",
            phoneNumber = "981147474",
            address = "Test Address",
            sex = "male"
        )

        self.profile2 = Profile.objects.create(
            name = "Test Name",
            phoneNumber = "123456789",
            address = "Test address",
            sex = "female"
        )

    def test_profile_model(self):
        self.assertEqual(self.profile1.name, "Test Test")
        self.assertEqual(self.profile2.phoneNumber, "123456789")
        self.assertEqual(self.profile1.sex, "male")
        self.assertEqual(self.profile2.sex, "female")
    
    def test_str_profile(self):
        self.assertEqual(str(self.profile1),"Test Test")
        self.assertEqual(str(self.profile2),"Test Name")
