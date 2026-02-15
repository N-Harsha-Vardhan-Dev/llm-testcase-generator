from app.llm_client import call_llm
from app.validator import validate_output

def safe_generate(prompt: str, retries: int = 2):
    """
    Calls LLM and validates output.
    Retries if JSON is invalid or schema fails.
    """

    for attempt in range(retries):
        raw_output = call_llm(prompt)

        try:
            return validate_output(raw_output)

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == retries - 1:
                raise ValueError(f"LLM output invalid after retries: {e}")

            # reinforce instructions for retry
            prompt += "\nReminder: Return ONLY valid JSON with all required fields."
