from django.core.management.base import BaseCommand
from books.models import Book
import json


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('fixtures/books.json', encoding='UTF-8') as f:
            books = json.load(f)

        for book in books:
            b = Book(
                name=book['fields']['name'],
                author=book['fields']['author'],
                pub_date=book['fields']['pub_date']
            )
            b.save()
