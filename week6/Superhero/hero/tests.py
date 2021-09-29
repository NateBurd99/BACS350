from django.test import TestCase
from .models import hero

class HeroTest(TestCase):

    def test_django(self):
        self.assertTrue
    
    def test_num_hero(self):
        self.assertEqual(len(hero.objects.all()), 0)

    def test_add_book(self):
        hero.objects.create(name='TestMan', description = 'Im a test dummy')
        self.assertEqual(len(hero.objects.all(),1))

# Create your tests here.
