from typing import TYPE_CHECKING
from typing import List

if TYPE_CHECKING:
    from docai.hints import Document
    from docai.hints import Layout


class ParserHelper:
    document: 'Document'

    def __init__(self, document: 'Document') -> None:
        self.document = document

    def get_text(self, layout: 'Layout') -> str:
        pieces: List[str] = []

        for segment in layout.text_anchor.text_segments:  # type: ignore
            text_start = (
                int(segment.start_index)
                if segment in layout.text_anchor.text_segments  # type: ignore
                else 0
            )

            text_end = int(segment.end_index)

            pieces.append(
                    self.document.text[text_start:text_end])  # type: ignore

        return ''.join(pieces)
