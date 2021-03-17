FROM relaysh/core:latest-python
COPY "./handler.py" "/trigger-azure-eventgrid.py"
ENTRYPOINT []
CMD ["python3", "/trigger-azure-eventgrid.py"]

LABEL "org.opencontainers.image.title"="Azure Event Grid trigger"
LABEL "org.opencontainers.image.description"="This trigger takes in the contents of an Azure Event Grid event and presents it as an output event"
LABEL "sh.relay.sdk.version"="v1"
