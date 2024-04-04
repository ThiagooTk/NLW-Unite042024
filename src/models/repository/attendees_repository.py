from typing import Dict, List
from src.models.settings.connection import db_connection_handler
from src.models.entities.attendees import Attendees
from src.models.entities.check_ins import CheckIns
from src.models.entities.events import Events
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import NoResultFound

class AttendeesRepository:
  def insert_attendee(self, ateendee_info: Dict) -> Dict:
    with db_connection_handler as database:
      try:
        attendee = (
          Attendees(
            id = ateendee_info.get("uuid"),
            name= ateendee_info.get("name"),
            email= ateendee_info.get("email"),
            event_id= ateendee_info.get("event_id"),
          )
        )
        database.session.add(attendee)
        database.session.commit()

        return ateendee_info
      except IntegrityError:
        raise Exception("Participante ja cadastrado!")
      except Exception as exception:
        database.session.rollback()
        raise exception
      
  def get_attendee_badge_by_id(self, attemdee_id: str) -> Attendees:
    with db_connection_handler as database:
      try:
        attendee = (
          database.session
            .query(Attendees)
            .join(Events, Events.id == Attendees.event_id)
            .filter(Attendees.id == attemdee_id)
            .with_entities(
              Attendees.name,
              Attendees.email,
              Events.title
            )
            .one()
        )
        return attendee
      except NoResultFound:
        return None
      except Exception as exception:
        database.session.rollback()
        raise exception
      
  def get_attendees_by_event_id(self, event_id: str) -> List[Attendees]:
    with db_connection_handler as database:
      ateendees = (
        database.session
        .query(Attendees)
        .outerjoin(CheckIns, CheckIns.attendeeId == Attendees.id)
        .filter(Attendees.event_id == event_id)
        .with_entities(
          Attendees.id,
          Attendees.name,
          Attendees.email,
          CheckIns.created_at.label("checkedInAt"),
          Attendees.created_at.label("createdAt")
        )
        .all()
      )
      return ateendees