# azure-eventgrid-trigger-event-fired

This trigger passes through events fired from Azure EventGrid. 

The payload will be wrapped in a map called `webhook_contents` and needs 
to be unwrapped at the step level in order touse it; see the example below.

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
