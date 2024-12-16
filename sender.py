from twilio.rest import Client
from bot.config import settings


class Twilio:
    """"""

    def client(self):
        """"""
        return Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

    def post(self, template_sid: str, variables: str):
        """"""

        try:
            MESSAGE = self.client().messages.create(
                from_=settings.WHATSAPP_FROM,
                content_sid=template_sid,
                content_variables=variables,
                to=settings.WHATSAPP_TO,
            )
            print("SENT MESSAGE:", MESSAGE.sid)
        except Exception as exc:
            print("ERROR:", exc)


if __name__ == "__main__":
    message = Twilio()
    message.post(
        template_sid=settings.CHOOSE_OPTIONS_TEMPLATE_SID,
            variables='''{
                "1": "*Pizzaria da Joselma*",
                "2": "Faça sua escolha:",
                "3": "Tradicionais",
                "4": "Especiais",
                "5": "Doces"
            }'''    
        )
