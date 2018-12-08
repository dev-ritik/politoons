from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Politoon
from .serializers import ToonsSerializer


# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_toon(name="", majorRole="", party=""):
        if name != "" and majorRole != "" and party != "":
            Politoon.objects.create(name=name, majorRole=majorRole, party=party, dob='2012-11-11', date='2012-11-11')

    def setUp(self):
        # add test data
        self.create_toon("Ritik kumar", "President", "Republic")
        self.create_toon("yess you", "devs", "labourers")


class GetAllPolitoonTest(BaseViewTest):

    def test_get_all_Politoon(self):
        """
        This test ensures that all Politoon added in the setUp method
        exist when we make a GET request to the Politoon/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("toons-all")
        )
        data = response.data
        print(response.status_code)
        print(data)

        # fetch the data from db
        expected = Politoon.objects.all()
        serialized = ToonsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
