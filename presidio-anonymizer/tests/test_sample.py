import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    text = "My name is Bond."
    start, end = 11, 15
    result = sample_run_anonymizer(text, start, end)

    # Check anonymized text
    assert result.text == "My name is BIP."

    # Check there is exactly 1 item
    assert len(result.items) == 1

    # Check item details (exact format)
    assert result.items[0].start == 11
    assert result.items[0].end == 14   # inclusive end
    assert result.items[0].entity_type == "PERSON"
    assert result.items[0].text == "BIP"
    assert result.items[0].operator == "replace"
