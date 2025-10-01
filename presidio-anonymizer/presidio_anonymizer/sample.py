from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text: str, start: int, end: int):
    engine = AnonymizerEngine()
    recognizer_result = RecognizerResult(
        entity_type="PERSON",
        start=start,
        end=end,  # exclusive
        score=0.8
    )

    result = engine.anonymize(
        text=text,
        analyzer_results=[recognizer_result],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}
    )

    return result

if __name__ == "__main__":
    res = sample_run_anonymizer("My name is Bond", 11, 15)
    print(res)