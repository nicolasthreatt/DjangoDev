from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from statsnba.models import Player
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

# VACCINES_NAMES = [
#     'Canine Parvo',
#     'Canine Distemper',
#     'Canine Rabies',
#     'Canine Leptospira',
#     'Feline Herpes Virus 1',
#     'Feline Rabies',
#     'Feline Leukemia'
# ]

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the player data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from player_data.csv into our Player model"

    def handle(self, *args, **options):
        
        if Player.objects.exists():
            print('Player data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        # print("Creating vaccine data")
        # for vaccine_name in VACCINES_NAMES:
        #     vac = Vaccine(name=vaccine_name)
        #     vac.save()
        print("Loading player data for players available for adoption")
        for row in DictReader(open('./player_data.csv')):
            
            player = Player()
            
            # Update Stats
            #   FIXME: MOVE TO A FUNCTION
            player.name       = row['Player']
            player.team       = row['Team']
            player.jersey_num = row['Jersey Number']
            player.ppg        = row['PPG']
            player.fg_p       = row['FG%']
            player.tp_p       = row['3P%']
            player.reb        = row['RPG']
            player.ast        = row['APG']

            # Update date
            #   FIXME: MOVE TO A FUNCTION
            raw_submission_date = row['Date']
            submission_date = UTC.localize(
                datetime.strptime(raw_submission_date, DATETIME_FORMAT))
            player.date = submission_date

            # Save data
            player.save()

            # raw_vaccination_names = row['vaccinations']
            # vaccination_names = [name for name in raw_vaccination_names.split('| ') if name]
            # for vac_name in vaccination_names:
            #     vac = Vaccine.objects.get(name=vac_name)
            #     player.vaccinations.add(vac)
            # player.save()
