from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text: str, start: int, end: int, new_value: str = "BIP"):
    # Initialize the engine
    engine = AnonymizerEngine()
    recognizer_result = RecognizerResult(
        entity_type="PERSON", 
        start=start,
        end=end, 
        score=0.8
    )

    # Invoke the anonymize function with the text, 
    # analyzer results (potentially coming from presidio-analyzer) and
    # Operators to get the anonymization output:
    result = engine.anonymize(
        text=text,
        analyzer_results=[(recognizer_result)],
        operators={"PERSON": OperatorConfig("replace", {"new_value": new_value})}
    )

    return result

    # input should be:
    # text: My name is Bond.
    # start: 11
    # end: 15
    # 
    # output should be:
    # text: My name is BIP.
    # items:
    # [
    #     {'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}
    # ]

if __name__ == "__main__": 
    res = sample_run_anonymizer("My name is Bond.", 11, 15)
    
    print(res)
