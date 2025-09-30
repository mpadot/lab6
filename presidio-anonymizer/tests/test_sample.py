import pytest
from presidio_anonymizer.sample import sample_run_anonymizer


def test_sample_run_anonymizer():
    # replace the following line with your test

    text = "My name is Bond."
    start = 11
    end = 15
    new_value = "BIP"

    # Expected
    expected_text = "My name is BIP."
    expected_items = [
        {'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}
    ]

    

    result = sample_run_anonymizer(text, start, end, new_value)

    print(result.items)
   

   
    


    
    