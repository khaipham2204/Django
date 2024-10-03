import pytest
from channels.testing import WebsocketCommunicator
from core.asgi import application

@pytest.mark.asyncio
async def test_websocket_connection():
    # Communicator
    communicator = WebsocketCommunicator(application, "/ws/chat/")
    
    # Connected:
    connected, _ = await communicator.connect()
    assert connected
    
    # Send messages:
    message = {"message":"hi"}
    await communicator.send_json_to(message)
    
    # Receive messages:
    response = await communicator.receive_json_from()
    assert response == {"message":"hi"}
    
    # Close the WebSocket connection
    await communicator.disconnect()
