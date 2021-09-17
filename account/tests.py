from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from .models import Account, Roles
from Organization.models import Organization

class TestDeviceSession(APITestCase):
    def setUp(self):
        username, password = self.create_admin()
        self.token = self.get_admin_token(username, password)
        self.org = "devtestorg121"
        Organization.objects.create(Org_name=self.org, Address="devtestorg121",
                                                   Description="devtestorg121", Number_of_emp=121)
        username = "mnauf"
        self.create_new_user()
        self.target = {
            "name": username
        }

    def create_admin(self):
        username = "shakeeb@retrocausal.ai"
        password = "abc12345"
        superUser = Account()
        superUser.username = "shakeeb"
        superUser.email = username
        superUser.set_password(password)
        superUser.is_admin = True
        superUser.is_active = True
        superUser.is_staff = True
        superUser.is_superuser = True
        superUser.save()

        return username, password

    def get_admin_token(self, username, password):
        url = reverse("account_api:login")

        data = {
            "username": username,
            "password": password
        }

        response = self.client.post(url, data=data, format="json")
        token = response.data["token"]
        return token

    def create_new_user(self):
        url = reverse("account_api:register")
        data = {
            "username": "mnauf",
            "lastname": "mnauf",
            "password": "abc12345",
            "confirm_password": "abc12345",
            "email": "m.naufil1@gmail.com",
            "phone_nomber": "0300-2222222",
            "position": "user"
        }
        self.client.post(url, data=data)

    def create_roles(self, roles):
        role_objs = (Roles(name=item) for item in roles)
        Roles.objects.bulk_create(role_objs)

    def test_create_new_user(self):
        url = reverse("account_api:register")
        data = {
            "username": "postman",
            "lastname": "postman",
            "password": "abc12345",
            "confirm_password": "abc12345",
            "email": "postman@retrocausal.ai",
            "phone_nomber": "0300-2222222",
            "position": "user"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.data, {'response': 'successfully registered new user.'})

    def test_approve_user(self):
        url = reverse("account_api:approve_user")
        data = {
            "email": "m.naufil1@gmail.com",
            # "Organization_name": "devtestorg121"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        response = self.client.put(url, data=data,
                                   **{'Authorization': f'Token {self.token}'}, format="json")
        self.client.credentials()
        self.assertEqual(response.data, {'User approved successfully'})

    def test_login_user(self):
        self.test_approve_user()
        url = reverse("account_api:login")
        data = {
            "username": "m.naufil1@gmail.com",
            "password": "abc12345"
        }
        self.client.credentials()
        response = self.client.post(url, data=data)
        user = response.data
        self.assertEqual(user["name"],self.target["name"])

    def test_assign_user_org(self):
        url = reverse("account_api:assign_user_org")
        data = {
            "email": "m.naufil1@gmail.com",
            "Organization_name": "devtestorg121"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.put(url, data=data)
        self.client.credentials()
        self.assertEqual(response.data, {'success': 'assign successfully'})

    def test_create_role(self):
        role_name = 'test_role'
        url = reverse('account_api:create_role')
        data = {
            'name': role_name
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data=data)
        self.assertEqual(response.data['name'], role_name)

    def test_list_roles(self):
        roles = ['test_role1', 'test_role2']
        self.create_roles(roles)
        url = reverse('account_api:create_role')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.get(url)
        self.assertEqual(len(response.data), 2)