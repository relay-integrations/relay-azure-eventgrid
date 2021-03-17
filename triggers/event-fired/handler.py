from relay_sdk import Interface, WebhookServer
from quart import Quart, request, jsonify, make_response

import logging
import json

relay = Interface()
app = Quart('azure-event')

logging.getLogger().setLevel(logging.INFO)


@app.route('/', methods=['POST'])
async def handler():
    subscription_validation = request.headers.get('aeg-event-type')

    # Perform the subscription validation of the webhook - Details here: https://docs.microsoft.com/en-us/azure/event-grid/webhook-event-delivery
    if subscription_validation == 'SubscriptionValidation':
        payload = await request.get_json()
        logging.info("Received the following webhook payload: \n%s", json.dumps(payload, indent=4))
        logging.info("Validating webhook subscription with Azure")
        return {'validationResponse': payload[0]['data']['validationCode']}, 200, {}

    # If webhook subscription is validated, start receiving events.
    event_payload = await request.get_json()
    logging.info("Received the following webhook payload: \n%s", json.dumps(event_payload, indent=4))

    if event_payload is None:
        return{'message': 'not a valid Azure EventGrid event'}, 400, {}

    # Emit the event payload to Relay
    relay.events.emit({
        'webhook_contents': event_payload
    })

    return {'message': 'success'}, 200, {}

if __name__ == '__main__':
    WebhookServer(app).serve_forever()
