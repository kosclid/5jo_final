from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
import csv
import re
from dictionary.models import Dictionganada


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        with open(
            "가나다라마바사.csv", encoding="utf8"
        ) as csv_file_sub_categories:
            rows = csv.reader(csv_file_sub_categories)
            next(rows, None)
            for row in rows:
                image_path = (
                    settings.BASE_DIR
                    / "dictionary"
                    / "assets"
                    / "img"
                    / "{}.png".format(row[0])
                )

                with image_path.open("rb") as f:
                    file = File(f)
                    dictionganada = Dictionganada()
                    dictionganada.lang_name = row[0]
                    dictionganada.lang_text = row[1]
                    dictionganada.lang_img.save(image_path.name, file, save=False)
                    dictionganada.lang_initial = row[2]
                    dictionganada.save()
                print(row[0])
            print("end done")
