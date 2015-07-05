from django.contrib.auth import get_user_model
User = get_user_model()

from django.test import TestCase
from django.http import HttpRequest
from django.utils.html import escape

from lists.views import new_list
from lists.models import Item, List
from lists.forms import EMPTY_ITEM_ERROR
        
class NewListViewIntegratedTest(TestCase):    

    def test_saving_a_POST_request(self):
        self.client.post('/lists/new',data={'text':'A new list item'})
        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')

    def test_for_invalid_input_doesnt_save_but_shows_errors(self):
        response = self.client.post('/lists/new',data={'text':''})
        self.assertEqual(List.objects.count(),0)
        self.assertContains(response,escape(EMPTY_ITEM_ERROR))

    def test_saves_list_owner_if_user_logged_in(self):
        request = HttpRequest()
        request.user = User.objects.create(email='a@b.com')
        request.POST['text'] = 'new list item'
        new_list(request)
        list_ = List.objects.first()
        self.assertEqual(list_.owner,request.user)
