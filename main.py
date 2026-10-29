import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Gamelib.settings")

django.setup()

from Librari.models import Game, Genre
# Genre.objects.create(
#     name = "Екшн")
# Genre.objects.create(name = "Рольові ігри")
# Genre.objects.create(name = "Шутер")
Ekchen = Genre.objects.get(id = 1)
RPG = Genre.objects.get(id = 3)
Shooter = Genre.objects.get(id = 4)
# print(ekchen.name,RPG.name,Shooter.name)
# Game.objects.create(name = "GTA5",date="2013-9-17",rating="8.5")
# Game.objects.create(name = "The Witcher 3",date="2015-3-19",rating="8.3")
# Game.objects.create(name = "Doom",date="1993-12-10",rating="8.5")
GTA5 = Game.objects.get(id=1)
Witcher3 = Game.objects.get(id=2)
Doom = Game.objects.get(id=3)

GTA5.genre.add(Ekchen)
Witcher3.genre.add(RPG)
Doom.genre.add(Shooter)
