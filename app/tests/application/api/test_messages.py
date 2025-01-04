from faker import Faker
from fastapi import FastAPI, status
from fastapi.testclient import TestClient

import httpx

import pytest


@pytest.mark.asyncio
def test_create_chat_success(app: FastAPI, client: TestClient, faker: Faker):

    url = app.url_path_for('create_chat_handler')
    title = faker.text(max_nb_chars=30)
    response: httpx.Response = client.post(url=url, json={'title': title})

    assert response.is_success
    json_data = response.json()

    assert json_data.get('title') == title


@pytest.mark.asyncio
def test_create_chat_fail_text_too_long(app: FastAPI, client: TestClient, faker: Faker):

    url = app.url_path_for('create_chat_handler')
    title = faker.text(max_nb_chars=3500)
    response: httpx.Response = client.post(url=url, json={'title': title})

    assert response.status_code == status.HTTP_400_BAD_REQUEST

    json_data = response.json()
    assert json_data['detail']


@pytest.mark.asyncio
def test_create_chat_fail_title_is_empty(app: FastAPI, client: TestClient, faker: Faker):

    url = app.url_path_for('create_chat_handler')
    response: httpx.Response = client.post(url=url, json={'title': ''})

    assert response.status_code == status.HTTP_400_BAD_REQUEST

    json_data = response.json()
    assert json_data['detail']