from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand
from django.utils.text import slugify

class Command(BaseCommand):
    # help = 'This comands inserts post data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        Category.objects.all().delete()

        categories = ['Sports', 'Technology', 'Science', 'Art', 'Food']



        for category_name in categories:
            Category.objects.create(name=category_name)
        self.stdout.write(self.style.SUCCESS("Completed inserting category data."))