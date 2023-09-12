from django.test import TestCase
from rest_framework.test import APIClient,APITestCase
from stage2.models import Person

class PersonApiTest(APITestCase):
    def setUp(self) -> None:
        self.client=APIClient()
        self.testData={
            "name":"Ayo"
        }
        person=Person.objects.create(name='Emmanuel_Ayomide')
        self.id=person.id
        self.expect=person.name
    def test_list(self):
        resp=self.client.get('/api/')
        self.assertEqual(resp.status_code,200)
        self.assertIsInstance(resp.data,list)
    def test_crud(self):
    # test Get operation
        resp=self.client.get(f'/api/{self.id}')
        self.assertEqual(resp.data["name"],self.expect)
    # test Post operation
        resp=self.client.post('/api/',self.testData, format='json')
        self.assertEqual(resp.status_code,201)
        self.assertEqual(resp.data['name'],self.testData['name'])
    # test Patch operation
        resp=self.client.patch(f"/api/{self.id}",self.testData, format='json')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(resp.data["name"],self.testData['name'])
    # test Delete Operation
        resp=self.client.delete('/api/2')
        self.assertEqual(resp.status_code,204)


