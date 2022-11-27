from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
import csv
from dictionary.models import Article


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        with open(
            "수화기사6개.csv", encoding="utf8"
        ) as csv_file_sub_categories:
            rows = csv.reader(csv_file_sub_categories)
            next(rows, None)
            for row in rows:
                image_path = (
                    settings.BASE_DIR
                    / "dictionary"
                    / "assets"
                    / "article"
                    / "{}.png".format(row[0])
                )

                with image_path.open("rb") as f:
                    file = File(f)
                    article = Article()
                    article.art_name = row[1]
                    article.art_link = row[2]
                    article.art_img.save(image_path.name, file, save=False)
                    article.art_from = row[0]
                    article.save()
                print(row[1])
            print("end done")
