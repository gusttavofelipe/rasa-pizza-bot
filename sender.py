from twilio.rest import Client
from pizzabot.config import settings


class Twilio:
    """"""

    def client(self):
        """"""
        return Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

    def post_message(self, template_sid: str, tracker=None,):
        """"""

        try:
            MESSAGE = self.client().messages.create(
                from_=settings.WHATSAPP_FROM,
                to=settings.WHATSAPP_TO,
                content_sid=template_sid,
            )
            print("MENSAGEM ENVIADA:", MESSAGE.sid)
        except Exception as exc:
            print("OCORREU UM ERRO:", exc)


twilio = Twilio()
twilio.post_message(settings.TEMPLATE_SID)
