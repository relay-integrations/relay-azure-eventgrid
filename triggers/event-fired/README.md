# azure-eventgrid-trigger-event-fired

This trigger passes through events fired from Azure EventGrid. 

The payload will be wrapped in a map called `webhook_contents` and needs 
to be unwrapped at the step level in order to use it; see the example below.

## Azure Configuration

You'll need to create an Azure Event Grid [Event Subscription](https://docs.microsoft.com/en-us/azure/event-grid/concepts#event-subscriptions) for the Event Grid "System Topic" you want to start receiving events from. When configuring the Event Subscription, select "Web Hook" and paste the webhook provided by Relay into the Subscriber Endpoint field.  

## Example Usage

```yaml
parameters:
  webhook_contents:
    description: "The full json payload from the incoming Azure EventGrid webhook"
triggers:
  - name: azure-eventgrid-event
    source:
      type: webhook
      image: relaysh/azure-eventgrid-trigger-event-fired
    binding:
      parameters:
        webhook_contents: !Data webhook_contents
steps:
  - name: dump-payload
    image: relaysh/core
    spec:
      webhook_contents: !Parameter webhook_contents
    input:
      - mkdir -p /azure/workflow
      - "ni get | jq .webhook_contents > /azure/workflow/event.json"
      - cat /azure/workflow/event.json
```
