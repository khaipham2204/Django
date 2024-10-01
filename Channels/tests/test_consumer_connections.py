import pytest
from channels.testing import HttpCommunicator
from consumers import MyConsumer

@pytest.mark.asyncio
async def test_my_consumer():
    communicator = HttpCommunicator(MyConsumer.as_asgi(), "GET", "/test/")
    response = await communicator.get_response()
    assert response["body"] == b"test response"
    assert response["status"] == 200
