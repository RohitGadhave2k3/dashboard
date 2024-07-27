import json
import os
from django.core.management.base import BaseCommand
from api.models import DataPoint
from django.conf import settings
from django.utils import timezone
from datetime import datetime

class Command(BaseCommand):
    help = 'Import data from JSON file'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'C:\\Users\\gadha\\Downloads\\jsondata.json')

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            added_time = item.get('added')
            published_time = item.get('published')

            # Check if dates are valid and parse them
            if added_time:
                added_time = datetime.strptime(added_time, '%B, %d %Y %H:%M:%S')
                added_time = timezone.make_aware(added_time)
            else:
                added_time = None  # or handle as needed

            if published_time:
                published_time = datetime.strptime(published_time, '%B, %d %Y %H:%M:%S')
                published_time = timezone.make_aware(published_time)
            else:
                published_time = None  # or handle as needed

            # Handle empty fields
            start_year = item.get('start_year') if item.get('start_year') else None
            impact = item.get('impact') if item.get('impact') else None

            DataPoint.objects.create(
                end_year=item.get('end_year'),
                intensity=item.get('intensity'),
                sector=item.get('sector'),
                topic=item.get('topic'),
                insight=item.get('insight'),
                url=item.get('url'),
                region=item.get('region'),
                start_year=start_year,
                impact=impact,
                added=added_time,
                published=published_time,
                country=item.get('country'),
                relevance=item.get('relevance'),
                pestle=item.get('pestle'),
                source=item.get('source'),
                title=item.get('title'),
                likelihood=item.get('likelihood'),
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
