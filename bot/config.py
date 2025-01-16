from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    """
    A data class for storing environment-specific settings required for the project.

    Attributes:
        `ACCOUNT_SID: str` - The account SID for Twilio.
        `AUTH_TOKEN: str` - The authentication token for Twilio.
        `WHATSAPP_FROM: str` - The Twilio-provided phone number to send WhatsApp messages from.
        `WHATSAPP_TO: str` - The recipient's WhatsApp phone number.
        `WEBHOOK: str` - The webhook URL to handle incoming events.
    """

    ACCOUNT_SID: str = os.getenv("ACCOUNT_SID") # type: ignore
    AUTH_TOKEN: str = os.getenv("AUTH_TOKEN") # type: ignore
    WHATSAPP_FROM: str = os.getenv("WHATSAPP_FROM") # type: ignore
    WHATSAPP_TO: str = os.getenv("WHATSAPP_TO") # type: ignore 
    WEBHOOK: str = os.getenv("WEBHOOK") # type: ignore


@dataclass(frozen=True)
class TwilioTemplates:
    """
    A data class for storing Twilio message templates.

    Attributes:
        `SAMPLE_QUICK_REPLY: str` - A quick reply template string.
        `SAMPLE_LIST_PICKER: str` - A list picker template string.
    """

    SAMPLE_QUICK_REPLY: str = os.getenv(
        "SAMPLE_QUICK_REPLY"
    ) # type: ignore
    SAMPLE_LIST_PICKER: str = os.getenv("SAMPLE_LIST_PICKER") # type: ignore


settings = Settings()
twilio_templates = TwilioTemplates()
