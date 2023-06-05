from typing import Union, List

from domain.entity.post import Post
from domain.exception.repository import NotExistedDataError
from domain.interface.post_repository import PostRepository

class InMemoryPostRepository(PostRepository):
    def __init__(self) -> None:
        self.posts: List[Post] = []

    def get_by_id(self, id: int) -> Union[Post, None]:
        try:
            return next(post for post in self.posts if post.id == id)
        except StopIteration as e:
            raise NotExistedDataError from e

    def get_all(self) -> list[Post]:
        return self.posts

    def save(self, post: Post):
        if post.id is None:
            post.id = len(self.posts)
        self.posts.append(post)