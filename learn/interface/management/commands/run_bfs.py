from django.core.management.base import BaseCommand, CommandError
import os
from interface.learn_scripts.models import random_forest_3

 
 
class Command(BaseCommand):
    help = 'Command to do........'
 
    def add_argument(self, parser):
        pass
        
    def handle(self, *args, **options):
        try:
            # your logic here
            #a=os.system("python2 interface/learn_scripts/models/random_forest.py interface/learn_scripts/datasets/classifier_bfs.csv")
        	datafile="interface/learn_scripts/datasets/classifier_bfs.csv"
        	a=random_forest_3.main(datafile)
        	return a
            
        except Exception as e:
            CommandError(repr(e))

        