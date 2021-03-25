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

import pytest
from mixer.backend.django import mixer
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from howler.models import Post
from howler.serializers import PostSerializer


@pytest.fixture()
def post() -> Post:
    return mixer.blend(Post)


@pytest.fixture()
def request_factory() -> APIRequestFactory:
    return APIRequestFactory()


@pytest.fixture()
def get_request(request_factory) -> Request:
    return request_factory.get("/fake-url/")


@pytest.fixture()
def post_serializer(post: Post, get_request: Request):
    return PostSerializer(post, context={"request": get_request})


@pytest.mark.django_db
def test_should_have_expected_fields(post_serializer: PostSerializer):
    assert list(post_serializer.data.keys()) == ["id", "url", "title", "authors", "creation_date", "content"]