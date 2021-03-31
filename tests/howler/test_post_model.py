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

from django.db.utils import IntegrityError
from mixer.backend.django import mixer

from howler.models import Post


@pytest.fixture()
def post() -> Post:
    return mixer.blend(Post)


@pytest.mark.django_db
def test_id_should_be_14_characters_long(post: Post):
    assert len(post.id) == 14


@pytest.mark.django_db
def test_id_must_be_unique(post: Post):
    with pytest.raises(IntegrityError):
        mixer.blend(Post, id=post.id)


@pytest.mark.django_db
def test_absolute_url_should_use_id(post: Post):
    assert post.get_absolute_url() == f"/post/{post.id}/"
