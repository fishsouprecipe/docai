from typing import TYPE_CHECKING
from typing import Dict
from typing import Union
from typing import cast

from google.cloud import documentai_v1beta3 as documentai

from docai.helpers import ParserHelper

if TYPE_CHECKING:
    from docai.processor_info import ProcessorInfo
    from docai.hints import File
    from docai.hints import Document
    from docai.hints import Page
    from docai.hints import FormField

from .base import BaseParser

FormParserOutput = Dict[str, Union[str, bool]]


class FieldValueType:
    FilledChechbox = 'filled_checkbox'
    UnfilledChechbox = 'unfilled_checkbox'
    Blank = ''


def parse_document(document: 'Document') -> 'FormParserOutput':
    helper = ParserHelper(document)
    _ = helper.get_text

    output_dict: 'FormParserOutput' = {}

    page: 'Page'
    field: 'FormField'
    for page in document.pages:  # type: ignore
        for field in page.form_fields:  # type: ignore
            name = (
                _(field.field_name)  # type: ignore
                    .strip()
                    .rstrip(':')
            )
            value_type = field.value_type

            if value_type == FieldValueType.FilledChechbox:
                value = True

            elif value_type == FieldValueType.UnfilledChechbox:
                value = False

            elif value_type == FieldValueType.Blank:
                value = _(field.field_value).strip()  # type: ignore

            else:
                raise ValueError(
                    f'Unsupported field value type {value_type!r}'
                )

            output_dict[name] = value

    return output_dict


class FormParser(BaseParser['FormParserOutput']):
    processor_info: 'ProcessorInfo'

    def __init__(self, processor_info: 'ProcessorInfo') -> None:
        self.processor_info = processor_info
        self.client = documentai.DocumentProcessorServiceClient()


    def feed(self, file: 'File') -> 'FormParserOutput':
        with open(file, 'rb') as f:
            content = f.read()

        request = documentai.ProcessRequest({
            'name': self.processor_info.name,
            'document': {
                'content': content,
                'mime_type': 'application/pdf',
            },
        })

        result = self.client.process_document(request=request)
        document = cast('Document', result.document)

        return parse_document(document)
