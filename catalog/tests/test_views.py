from django.test import TestCase
from django.urls import reverse
from catalog.models import Author

class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(13):
            Author.objects.create(first_name=f'First{i}', last_name=f'Last{i}')

    def test_view_url_exists(self):
        response = self.client.get('/catalog/authors/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get(reverse('authors'))
        self.assertTemplateUsed(response, 'catalog/author_list.html')

    def test_pagination(self):
        response = self.client.get(reverse('authors'))
        self.assertTrue(response.context['is_paginated'])
        self.assertEqual(len(response.context['author_list']), 10)

    def test_second_page_has_three_authors(self):
        response = self.client.get(reverse('authors') + '?page=2')
        self.assertEqual(len(response.context['author_list']), 3)


from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Author
from django.contrib.auth import get_user_model
User = get_user_model()

class AuthorCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

        content_type = ContentType.objects.get_for_model(Author)
        permission = Permission.objects.get(codename='add_author', content_type=content_type)
        self.user.user_permissions.add(permission)
        self.user.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('author-create'))
        self.assertNotEqual(response.status_code, 200)

    def test_logged_in_with_permission_access(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('author-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/author_form.html')

    def test_initial_date_of_death(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('author-create'))
        self.assertEqual(response.context['form'].initial['date_of_death'], '2023-11-11')
