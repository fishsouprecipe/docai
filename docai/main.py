import pprint
import argparse
from pathlib import Path

from typing import Sequence
from typing import Optional

from docai.processor_info import ProcessorInfo
from docai.parsers import FormParser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--project-id', type=str, required=True)
    parser.add_argument('--processor-id', type=str, required=True)
    parser.add_argument('--location', type=str, default='us')
    parser.add_argument('file', type=Path)
    args = parser.parse_args(argv)

    processor_info = ProcessorInfo(
        project_id=args.project_id,
        location=args.location,
        processor_id=args.processor_id,
    )

    parser = FormParser(processor_info=processor_info)

    result = parser.feed(args.file)

    pprint.pprint(result)

    return 0
