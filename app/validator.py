import json
import re
from app.schema import TestCaseOutput

def extract_json(text: str) -> str:
    """
    Extract JSON from LLM response.
    Handles markdown fences and extra text.
    """

    # Remove markdown code fences if present
    text = re.sub(r"```json|```", "", text).strip()

    # find first valid JSON object 
    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        return match.group(0)
    
    raise ValueError("No valid JSON found in LLM output")


def validate_output(raw_output: str) -> TestCaseOutput:
    """
    Validate and parse LLM output into schema-defined structure.
    """
    try: 
        cleaned = extract_json(raw_output)
        data = json.loads(cleaned)
        return TestCaseOutput(**data)
    except json.JSONDecodeError as e: 
        raise ValueError(f"Invalid JSON format: {e}")
    except Exception as e:
        raise ValueError(f"Validation error: {e}")