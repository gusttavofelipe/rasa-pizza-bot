from twilio.rest import Client
from pizzabot.config import settings
from rasa_sdk.interfaces import Tracker


class Twilio:
    """"""

    def client(self):
        """"""
        return Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

    def post_message(self, template_sid: str, action_tracker: Tracker) -> None:
        """"""

        try:
            MESSAGE = self.client().messages.create(
                from_=settings.WHATSAPP_FROM,
                to=action_tracker.sender_id,
                content_sid=template_sid,
            )
            print("MENSAGEM ENVIADA:", MESSAGE.sid)
        except Exception as exc:
            print("OCORREU UM ERRO:", exc)


twilio = Twilio()
