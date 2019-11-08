from django.core.management.base import BaseCommand

from src.core.core import get_encoded_logs
from src.jobs.models import Job


class Command(BaseCommand):
    help = 'tries to deliver an explanation of a random prediction of the trained model'

    def handle(self, *args, **kwargs):
        # get model
        TARGET_MODEL = 18
        job = Job.objects.filter(pk=TARGET_MODEL)[0]

        # load data
        training_df, test_df = get_encoded_logs(job)  # todo qui vedi statistiche prefix

        # extract items
        # trova tracce identiche
        # trova distribuzione attributi
        # e.g. suggerisci esecuzione evento 'as soon as you can'

        # encode items

        # try suggestion

        print('done')
