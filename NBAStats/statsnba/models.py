from django.db import models

class Player(models.Model):
    TEAM_CHOICES = [('ATL', 'Atlanta Hawks'),
                    ('BOS', 'Boston Celtics'),
                    ('BYN', 'Brookyln Nets'),
                    ('CHA', 'Charlotte Hornets'),
                    ('CHI', 'Chicago Bulls'),
                    ('CLE', 'Cleveland Cavaliers'),
                    ('DAL', 'Dallas Mavericks'),
                    ('DEN', 'Denver Nuggets'),
                    ('DET', 'Detriot Pistons'),
                    ('GSW', 'Golden State Warriors'),
                    ('HOU', 'Houston Rockets'),
                    ('IND', 'Indiana Pacers'),
                    ('LAC', 'LA Clippers'),
                    ('LAL', 'Los Angeles Lakers'),
                    ('MEM', 'Memphis Grizzlies'),
                    ('MIA', 'Miami Heat'),
                    ('MIL', 'Milwaukee Bucks'),
                    ('MIN', 'Minnesota Timberwolves'),
                    ('NOP', 'New Orleans Pelicans'),
                    ('NYK', 'New York Knicks'),
                    ('OKC', 'Oklahoma City Thunder'),
                    ('ORL', 'Orlando Magic'),
                    ('PHI', 'Philadelphia 76ers'),
                    ('PHX', 'Phoenix Suns'),
                    ('POR', 'Portland Trail Blazers'),
                    ('SAC', 'Sacramento Kings'),
                    ('SAS', 'San Antonio Spurs'),
                    ('TOR', 'Toronto Raptors'),
                    ('UTA', 'Utah Jazz'),
                    ('WAS','Washington Wizards')
                   ]

    id         = models.AutoField(primary_key=True)
    name       = models.CharField(max_length=100)
    team       = models.CharField(choices=TEAM_CHOICES, max_length=3)
    jersey_num = models.IntegerField()
    
    ppg        = models.DecimalField(max_digits=3, decimal_places=1)
    fg_p       = models.DecimalField(max_digits=3, decimal_places=1)
    tp_p       = models.DecimalField(max_digits=3, decimal_places=1)
    reb        = models.DecimalField(max_digits=3, decimal_places=1)
    ast        = models.DecimalField(max_digits=3, decimal_places=1)
    
    date       = models.DateTimeField()

# class Skills(models.Model):
#     skill = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name