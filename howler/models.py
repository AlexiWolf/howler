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

from django.db import models
from random_id import random_id


class Post(models.Model):
    """
    The Post model stores text-only content and other basic information about a blog
    post such as the title, creation / publish date, and a list of authors.  The Post
    class also provides a number of convenience methods to make interacting with posts
    more intuitive.

    As stated above, Posts only store the text content of the blog post.  This is an
    intentional choice to keep the Post class focused on a single job.  Media should be
    handled by a separate system, such as a one-to-many relationship with another model.
    This is how the Howler Media extension is intended to function.
    """

    id = models.CharField(
        primary_key=True,
        max_length=14,
        default=random_id,
        editable=False,
        blank=False,
        null=False,
        help_text="Randomly generated unique id.  This is not meant to be edited.",
    )
