import pytest
from httpx import AsyncClient
import os

test_params = {
    'pickup_datetime': '2013-07-06 17:18:00',
    'pickup_longitude': '-73.950655',
    'pickup_latitude': '40.783282',
    'dropoff_longitude': '-73.984365',
    'dropoff_latitude': '40.769802',
    'passenger_count': '1'
}

TEST_ENV = os.getenv("TEST_ENV")


@pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
@pytest.mark.asyncio
async def test_root_is_up():
    from taxifare.api.fast import app
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200


@pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
@pytest.mark.asyncio
async def test_root_returns_greeting():
    from taxifare.api.fast import app
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.json() == {"greeting": "Hello"}


@pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
@pytest.mark.asyncio
async def test_predict_is_up():
    from taxifare.api.fast import app
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/predict", params=test_params)
    assert response.status_code == 200


@pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
@pytest.mark.asyncio
async def test_predict_is_dict():
    from taxifare.api.fast import app
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/predict", params=test_params)
    assert isinstance(response.json(), dict)
    assert len(response.json()) == 1


@pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
@pytest.mark.asyncio
async def test_predict_has_key():
    from taxifare.api.fast import app
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/predict", params=test_params)
    assert response.json().get('fare_amount', False) or response.json().get('fare', False)


@pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
@pytest.mark.asyncio
async def test_predict_val_is_float():
    from taxifare.api.fast import app
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/predict", params=test_params)
    assert isinstance(response.json().get('fare_amount'), float) or isinstance(response.json().get('fare'), float)


# @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
# @pytest.mark.asyncio
# async def test_predict_val_is_in_range():
#     from taxifare.api.fast import app
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/predict", params=test_params)
#     popularity = response.json()['popularity']
#     assert popularity > 21
#     assert popularity < 23


# @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
# @pytest.mark.asyncio
# async def test_predict_val_change_with_params():
#     alt_params = {
#         "acousticness": 0.521,
#         "danceability": 0.358,
#         "duration_ms": 413947,
#         "energy": 0.48,
#         "explicit": 0,
#         "id": "3TO7bbrUKrOSPGRTB5MeCz",
#         "instrumentalness": 0.00428,
#         "key": 9,
#         "liveness": 0.178,
#         "loudness": -11.79,
#         "mode": 1,
#         "name": "Time",
#         "release_date": "1973-03-01",
#         "speechiness": 0.0849,
#         "tempo": 120.317,
#         "valence": 0.356,
#         "artist": "Pink Floyd"
#     }
#     from taxifare.api.fast import app
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/predict", params=test_params)
#         alt_response = await ac.get("/predict", params=alt_params)
#     assert response.json().get('popularity') != alt_response.json().get('popularity')
