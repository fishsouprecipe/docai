from typing import NamedTuple
from typing import Union


class ProcessorInfo(NamedTuple):
    project_id: Union[int, str]
    location: str
    processor_id: str

    @property
    def name(self) -> str:
        return (
            f'projects/{self.project_id}/locations/'
            f'{self.location}/processors/{self.processor_id}'
        )
