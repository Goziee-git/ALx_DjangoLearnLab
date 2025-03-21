from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from relationship_app.models import Book, Author, UserProfile, create_user_profile, save_user_profile
from relationship_app.utils import (
    assign_admin_permissions, assign_librarian_permissions, assign_member_permissions
)

class BookPermissionTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Temporarily disconnect the signals
        post_save.disconnect(create_user_profile, sender=User)
        post_save.disconnect(save_user_profile, sender=User)

        # Create base test data
        cls.author = Author.objects.create(name='Test Author')
        #cls.book = Book.objects.create(title='Test Book', author=cls.author)

    def setUp(self):
        # Create users and their profiles manually
        self.admin_user = User.objects.create_user('admin', 'admin@test.com', 'adminpass')
        UserProfile.objects.create(user=self.admin_user, role='Admin')
        assign_admin_permissions(self.admin_user)

        self.librarian_user = User.objects.create_user('librarian', 'lib@test.com', 'libpass')
        UserProfile.objects.create(user=self.librarian_user, role='Librarian')
        assign_librarian_permissions(self.librarian_user)

        self.member_user = User.objects.create_user('member', 'member@test.com', 'memberpass')
        UserProfile.objects.create(user=self.member_user, role='Member')
        assign_member_permissions(self.member_user)

        # Create test book
        self.book = Book.objects.create(title='Test Book', author=self.author)

        # Get content type for Book model
        self.book_content_type = ContentType.objects.get_for_model(Book)

        # Create permissions
        self.view_permission = Permission.objects.get(
            codename='can_view_book',
            content_type=self.book_content_type,
        )
        self.add_permission = Permission.objects.get(
            codename='can_add_book',
            content_type=self.book_content_type,
        )
        self.edit_permission = Permission.objects.get(
            codename='can_edit_book',
            content_type=self.book_content_type,
        )
        self.delete_permission = Permission.objects.get(
            codename='can_delete_book',
            content_type=self.book_content_type,
        )

    def test_admin_can_add_book(self):
        '''Test that admin users can add books'''
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(reverse('add_book'), {
            'title': 'New Test Book',
            'author': self.author.id})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Book.objects.filter(title="New Test Book").exist())

    def test_librarian_can_edit_book(self):
        '''test that librarian can edit books'''
        self.client.login(username='librarian', password='libpass')
        response = self.client.post(reverse('edit_book', kwargs={'book_id': self.book.id}), {
            'title': 'Updated Book',
            'author': self.author.id
        })
        self.assertEqual(response.status_code, 302)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_member_can_only_view(self):
        '''test that members can only view books'''
        self.client.login(username='member', password='memberpass')
        response = self.client.get(reverse('list_books'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('add_book'),{
            'title': 'New Book',
            'author': self.author.id
        })

        self.assertEqual(response.status_code, 403)

    @classmethod
    def tearDownClass(cls):
        # Reconnect the signals
        post_save.connect(create_user_profile, sender=User)
        post_save.connect(save_user_profile, sender=User)
        super().tearDownClass()