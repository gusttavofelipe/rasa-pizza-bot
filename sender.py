from twilio.rest import Client
import env


account_sid = env.ACCOUNT_SID
auth_token = env.AUTH_TOKEN
whatsapp_from = env.WHATSAPP_FROM
whatsapp_to = env.WHATSAPP_TO
template = env.TEMPLATE_SID


client = Client(account_sid, auth_token)

message = client.messages.create(
    from_=whatsapp_from,
    to=whatsapp_to,
    content_sid=template,
)


print(f"MESSAGE SID: {message.sid}")
