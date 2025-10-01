import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    text = "My name is Bond."
    start, end = 11, 15
    engine_result = sample_run_anonymizer(text, start, end)

    # Check anonymized text
    assert engine_result.text == "My name is BIP."

    # Check there is exactly 1 item
    assert len(engine_result.items) == 1
    item = engine_result.items[0]

    # Check item details
    assert item.start == start
    assert item.end == end - 1   
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"
