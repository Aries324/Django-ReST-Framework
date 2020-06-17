from django.core.management.base import BaseCommand
from shoeapp.models import  ShoeColor, ShoeType

class Command(BaseCommand):
    help = 'Select the type of shoe and color'

    def handle(self, *args, **options):
        for shoe_type in ShoeType.SHOE_TYPE_CHOICES:
            ShoeType.objects.create(
                    style=shoe_type[0]
            )
            self.stdout.write(self.style.SUCCESS('Your shoe style "%s" has been added!' % shoe_type[1]))

        for shoe_color in ShoeColor.SHOE_COLOR_CHOICES:
            ShoeColor.objects.create(
                shoe_colors=shoe_color[0]
            )

            self.stdout.write(self.style.SUCCESS('Your shoe color "%s" has been added!' % shoe_color[1]))