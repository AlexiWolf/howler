#  Copyright (C) 2021 AlexiWolf
#
#  Howler is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  Howler is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with Howler.  If not, see <https://www.gnu.org/licenses/>.
from typing import Type

import pytest
from django.contrib.auth import get_user_model
from django.core.handlers.wsgi import WSGIRequest
from mixer.backend.django import mixer
from rest_framework.test import APIRequestFactory

from howler.models import Post
from howler.viewsets import PostViewSet

UserModel = get_user_model()


@pytest.fixture()
def post() -> Post:
    return mixer.blend(Post)


@pytest.fixture()
def api_request_factory() -> APIRequestFactory:
    return APIRequestFactory()


@pytest.fixture()
def get_request(api_request_factory: APIRequestFactory):
    return api_request_factory.get("/fake-url/")


@pytest.fixture()
def view_set() -> Type[PostViewSet]:
    return PostViewSet


@pytest.mark.django_db
def test_should_allow_anonymous_users_to_view_post_list(
        get_request: WSGIRequest, view_set: PostViewSet):
    view = view_set.as_view({"get": "list"})
    response = view(get_request)
    assert response.status_code == 200


@pytest.mark.django_db
def test_should_allow_anonymous_users_to_view_post_details(
        post: Post, get_request: WSGIRequest, view_set: PostViewSet):
    view = view_set.as_view({"get": "retrieve"})
    response = view(get_request, id=post.id)
    assert response.status_code == 200
