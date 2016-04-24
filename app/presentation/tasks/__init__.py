from celery import Celery

from app.application.services import handle_set_tags_for

BROKER_URL = 'redis://localhost:6379/0'

app = Celery('app.presentation.tasks', broker=BROKER_URL)

@app.task
def set_tags(entry_id):
    handle_set_tags_for(entry_id)


if __name__ == '__main__':
    # workon demoddd
    # celery -A app.presentation.tasks worker --loglevel=info
    set_tags.delay(1)
    set_tags.delay(2)
