import pytest
from presidio_anonymizer.sample import sample_run_anonymizer
@pytest.mark.parametrize(
    "text, start, end, new_value",
    [
        ("My name is Bond.", 11, 15, "BIP")
    ]
)



def test_sample_run_anonymizer(text, start, end, new_value):
    # Run function
    result = sample_run_anonymizer(text, start, end, new_value)

    # Expected text after anonymization
    expected_text = "My name is BIP."

    # Assertions
    assert result.text == expected_text
    assert len(result.items) == 1

    item = result.items[0]
    assert item.start == 11
    assert item.end == 14   
    assert item.text == "BIP"
    assert item.operator == "replace"
    assert item.entity_type == "PERSON"

   

   
    


    
    