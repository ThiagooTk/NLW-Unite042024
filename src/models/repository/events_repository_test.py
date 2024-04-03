import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Pular insert")
def test_insert_event():
  event = {
    "uuid": "xxx-uuid2",
    "title": "meu_title",
    "slug": "meu_slug2",
    "maximum_attendees": 20
  }

  event_repository = EventsRepository()
  response = event_repository.insert_event(event)
  print(response)

@pytest.mark.skip(reason="Pular query")
def teste_get_event_by_id():
  event_id = "xxx-uuidAAAA"
  event_repository = EventsRepository()
  response = event_repository.get_event_by_id(event_id)
  print(response)
