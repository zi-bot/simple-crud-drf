from django.test import TestCase

# Create your tests here.

class AddUserProfileTest(TestCase):
    def test_add_userprofile(self):
        payload = {
            'lname': 'test',
            'fname': 'test',
            'is_active': True,
        }
        response = self.client.post('/api/userprofile/', payload, content_type="application/json",format='json')
        self.assertEqual(response.status_code, 201)

    def test_add_userprofile_invalid(self):
        payload = {
            'fname': 'test',
            'is_active': True,
        }
        response = self.client.post('/api/userprofile/', payload, content_type="application/json",format='json')
        self.assertEqual(response.status_code, 400)

class UpdateUserProfileTest(TestCase):
    def setUp(self):
        payload = {
            'lname': 'test',
            'fname': 'test',
            'is_active': True,
        }
        response = self.client.post('/api/userprofile/',payload, content_type="application/json",format='json')
        self.assertEqual(response.status_code, 201)

    def test_update_userprofile(self):
        payload = {
            'lname': 'test',
            'fname': 'test',
            'is_active': True,
        }
        response = self.client.put('/api/userprofile/1/', payload, content_type="application/json",format='json')
        self.assertEqual(response.status_code, 200)

    def test_update_userprofile_invalid(self):
        payload = {
            'fname': 'test',
            'is_active': True,
        }
        response = self.client.put('/api/userprofile/1/', payload, content_type="application/json",format='json')
        self.assertEqual(response.status_code, 400)


class DeleteUserProfileTest(TestCase):
    def setUp(self):
        payload = {
            'lname': 'test',
            'fname': 'test',
            'is_active': True,
        }
        response = self.client.post('/api/userprofile/',payload, content_type="application/json",format='json')
        self.assertEqual(response.status_code, 201)

    def test_delete_userprofile(self):
        response = self.client.delete('/api/userprofile/1/', content_type="application/json",format='json')
        self.assertEqual(response.status_code, 204)

    def test_delete_userprofile_invalid(self):
        response = self.client.delete('/api/userprofile/2/', content_type="application/json",format='json')
        self.assertEqual(response.status_code, 404)


class GetUserProfileTest(TestCase):
    def setUp(self):
        payload = {
            'lname': 'test',
            'fname': 'test',
            'is_active': True,
        }
        response = self.client.post('/api/userprofile/',payload, content_type="application/json",format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_userprofile(self):
        response = self.client.get('/api/userprofile/1/', content_type="application/json",format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_userprofile_invalid(self):
        response = self.client.get('/api/userprofile/2/', content_type="application/json",format='json')
        self.assertEqual(response.status_code, 404)


class GetAllUserProfileTest(TestCase):
    def setUp(self):
        payload = {
            'lname': 'test',
            'fname': 'test',
            'is_active': True,
        }
        response = self.client.post('/api/userprofile/',payload, content_type="application/json",format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_userprofile(self):
        response = self.client.get('/api/userprofile/', content_type="application/json",format='json')
        self.assertEqual(response.status_code, 200)


class UserProfilePaginationTest(TestCase):
    def setUp(self):
        payload = {
            'lname': 'test',
            'fname': 'test',
            'is_active': True,
        }
        response = self.client.post('/api/userprofile/',payload, content_type="application/json",format='json')
        self.assertEqual(response.status_code, 201)

    def test_userprofile_pagination(self):
        response = self.client.get('/api/userprofile/', content_type="application/json",format='json')
        self.assertEqual(response.status_code, 200)

    def test_userprofile_pagination_invalid(self):
        response = self.client.get('/api/userprofile/?page=2', content_type="application/json",format='json')
        self.assertEqual(response.status_code, 200)