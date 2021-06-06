import abc
from typing import TYPE_CHECKING
from typing import Generic
from typing import TypeVar

if TYPE_CHECKING:
    from docai.hints import File

T = TypeVar('T')


class BaseParser(abc.ABC, Generic[T]):
    @abc.abstractmethod
    def feed(self, file: 'File') -> T:
        ...
