from typing import Union
from pathlib import Path
from google.cloud.documentai_v1beta3 import Document

File = Union[Path, str]
Page = Document.Page
FormField = Page.FormField
Paragraph = Page.Paragraph
Layout = Page.Layout
Number = Union[float, int]
