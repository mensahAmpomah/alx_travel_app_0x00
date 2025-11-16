from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = "Seed the database with sample listing data."

    def handle(self, *args, **kwargs):
        sample_listings = [
            {
                "title": "Beachfront Resort",
                "description": "A beautiful resort near the beach.",
                "price_per_night": 120.00,
                "location": "Cape Coast, Ghana",
                "available": True,
            },
            {
                "title": "Luxury Apartment",
                "description": "5-star apartment with ocean view.",
                "price_per_night": 200.00,
                "location": "Accra, Ghana",
                "available": True,
            },
            {
                "title": "Mountain Cabin",
                "description": "Quiet cabin with amazing scenery.",
                "price_per_night": 80.00,
                "location": "Aburi, Ghana",
                "available": False,
            },
        ]

        for data in sample_listings:
            Listing.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))