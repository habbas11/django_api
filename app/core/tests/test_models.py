from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):

    def test_create_user_email_successful(self):
        email = 'test@examle.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['test2@EXAMPLE.COM', 'test2@example.com'],
            ['Test3@example.COM', 'Test3@example.com'],
            ['TEST4@EXAMPLE.COM', 'TEST4@example.com'],
        ]

        for email, target in sample_emails:
            user = get_user_model().objects.create_user(
                email=email,
                password='sample123'
            )
            self.assertEqual(user.email, target)

    def test_user_email_empty(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'testPass123')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test123@example.com',
            '123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        user = get_user_model().objects.create_user(
            'test@examle.com',
            'testpass123',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Recipe Name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Recipe Description'
        )
        # print(f'\n\n Recipe {str(recipe)}\n\n')
        self.assertEqual(str(recipe), recipe.title)
