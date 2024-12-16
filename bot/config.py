from dataclasses import dataclass
import os


@dataclass
class Settings:
    """"""

    ACCOUNT_SID = os.getenv("ACCOUNT_SID")
    AUTH_TOKEN = os.getenv("AUTH_TOKEN")
    WHATSAPP_FROM = os.getenv("WHATSAPP_FROM")
    WHATSAPP_TO = os.getenv("WHATSAPP_TO")
    CHOOSE_OPTIONS_TEMPLATE_SID = os.getenv("CHOOSE_OPTIONS_TEMPLATE_SID")
    WEBHOOK = os.getenv("WEBHOOK")


settings = Settings()

# print(dir(settings))
