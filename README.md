# DocAI 🤖🧠 (Experimental)

## Installation

```bash
pip install --user git+https://github.com/fishsouprecipe/docai.git
```

## Manual Installation
```bash
git clone git@github.com:fishsouprecipe/docai.git /tmp/docai

pip --no-cache-dir --disable-pip-version-check install /tmp/docai
```

## CLI usage
```bash
docai-cli --project_id ... --processor_id ... [--location ...] <file>
```

### Arguments

Argument name | Type | Required | Default Value
-------- | ---- | -------- | -------------
--project-id | str | True | -
--processor-id | str | True | -
file | path | True | -
location | str | False | us


## Package Usage
```python
from docai.processor_info import ProcessorInfo
from docai.parsers import FormParser

file = '/resource/pdfs/form1.pdf'

processor_info = ProcessorInfo(
    project_id=...,
    location=...,
    processor_id=...,
)

parser = FormParser(processor_info=processor_info)

result = parser.feed(file)

assert isinstance(result, dict)
```
