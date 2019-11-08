import django_rq
from django.core.management.base import BaseCommand

from src.jobs import tasks


class Command(BaseCommand):
    help = 'helps requeue properly jobs that have been remove from both default and failed queue in redis'

    def handle(self, *args, **kwargs):
        jobs_to_requeue = [1065, 1064, 1035, 1034, 785, 480, 479, 476, 475, 474, 471, 479, 469, 466, 465, 464, 461,
                           450, 449, 446, 445, 444, 441, 440, 439, 436, 435, 434, 431, 420, 419, 416, 415, 414, 411,
                           410, 409, 406, 405, 404, 401, 390, 389, 386, 385, 381, 380, 379, 374, 371, 365, 220]
        print('Requeue of', jobs_to_requeue)
        [django_rq.enqueue(tasks.prediction_task, j) for j in jobs_to_requeue]
        print('done')
