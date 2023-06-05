from abc import ABCMeta, abstractmethod

from typing import Union

from domain.entity.post import Post

class PostRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_by_id(self, id: int) -> Union[Post, None]:
        pass

    @abstractmethod
    def get_all(self) -> list[Post]:
        pass

    @abstractmethod
    def save(self, post: Post) -> bool:
        pass
