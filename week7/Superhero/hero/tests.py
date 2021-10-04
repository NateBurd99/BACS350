from django.test import TestCase
from .models import hero

class HeroTest(TestCase):

    def test_django(self):
        self.assertTrue
    
    def test_num_hero(self):
        self.assertEqual(len(hero.objects.all()), 0)

    def test_add_hero(self):
        hero.objects.create(name='TestMan', description = 'Im a test dummy')
        self.assertEqual(len(hero.objects.all(),1))

    def test_hero_name(self):
        hero.objects.create(name='TestMan', description = 'Im a test dummy')
        h = hero.objects.get(pk=1)
        self.assertEqual(h.name, 'TestMan')

    def test_hero_edit(self):
        hero.objects.create(name='TestMan', description = 'Im a test dummy')
        h = hero.objects.get(pk=1)
        h.name = 'Test Man'
        h.save()
        self.assertEqual(h.name, 'Test Man')

    def test_hero_edit(self):
        hero.objects.create(name='TestMan', description = 'Im a test dummy')
        h = hero.objects.get(pk=1)
        h.delete()
        self.assertEqual(len(hero.objects.all()), 0)

