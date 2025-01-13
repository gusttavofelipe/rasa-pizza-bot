from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from msg.twilio_ import message
from bot.config import settings


class ActionGreet(Action):
    """"""

    def name(self) -> Text:
        return "action_stt_greet"

    def run(self, dispatcher, tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message.post(
            action_tracker=tracker,
            template_sid=settings.CHOOSE_OPTIONS_TEMPLATE_SID,
            variables='''{
                "1": "*Pizzaria da Joselma*",
                "2": "Faça sua escolha:",
                "3": "Tradicionais",
                "4": "Especiais",
                "5": "Doces"
            }'''

        )
        return []


class ActionSetPizzaType(Action):
    """"""

    def name(self) -> Text:
        return "action_set_pizza_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pizza_type = tracker.get_slot("pizza_type")

        if pizza_type:
            dispatcher.utter_message(text=f"{pizza_type}, ok! Agora escolha o tamanho, por favor.")
            return [SlotSet("pizza_type", pizza_type)]
        else:
            dispatcher.utter_message(text="Por favor, escolha o tipo de pizza.")
            return []
