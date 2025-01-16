from twilio.rest import Client
from bot.config import settings
from rasa_sdk.interfaces import Tracker


class Twilio:
    """
    A class for handling interactions with the Twilio API.

    Methods:
        `client() -> Client`:
            Creates and returns a Twilio API client instance.
        
        `post(template_sid: str, variables: str, action_tracker: Tracker) -> bool`:
            Sends a WhatsApp message using a specified template and variables.
    """

    def client(self) -> Client:
        """Creates and returns a Twilio API client instance."""
        return Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

    def post(
            self, template_sid: str, variables: str, action_tracker: Tracker
        ) -> bool:
        """
        Sends a WhatsApp message using the Twilio API.

        Parameters:
            `template_sid: str`
                The SID of the Twilio template to use for the message.
            `variables: str`
                The JSON string containing variables to populate the message template.
            `action_tracker: Tracker`
                The Rasa Tracker instance used to retrieve the sender's ID.

        Returns:
            bool: Returns `True` if the message was sent successfully.

        Raises:
            Exception: Logs any exceptions encountered while sending the message.
        """

        try:
            MESSAGE = self.client().messages.create(
                from_=settings.WHATSAPP_FROM,
                to=action_tracker.sender_id,
                content_sid=template_sid,
                content_variables=variables
            )
            print("MENSAGEM ENVIADA:", MESSAGE.sid)
        except Exception as exc:
            print("OCORREU UM ERRO:", exc)

        return True


message = Twilio()
