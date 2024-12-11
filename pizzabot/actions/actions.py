from messaging.twilio_ import twilio
from rasa_sdk import Action
from rasa_sdk.events import EventType
from rasa_sdk.types import DomainDict
from typing import List, Text
from pizzabot.config import settings


class SttGreet(Action):
    def name(self) -> Text:
        return "action_stt_greet"

    def run(
        self,
        dispatcher,
        tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        twilio.post_message(
            template_sid=settings.TEMPLATE_SID, action_tracker=tracker
        )
        return []
