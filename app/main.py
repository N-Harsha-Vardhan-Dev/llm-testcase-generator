from fastapi import FastAPI
from app.prompt import PROMPT_TEMPLATE
from app.llm_client import call_llm
from app.validator import validate_output
from app.llm_service import safe_generate
from app.exporter import export_to_csv
from app.coverage import calculate_coverage
app = FastAPI(title="LLM Test Case Generator")

@app.post("/generate-tests")
def generate_tests(requirement: str, save_file: bool = False):
    prompt = PROMPT_TEMPLATE.format(requirement=requirement)
    validated = safe_generate(prompt)

    coverage = calculate_coverage(validated.test_cases, validated.edge_cases)
    
    if save_file:
        file_name = export_to_csv(validated)
        return {"message": "Saved successfully", "file": file_name, "data": validated, "coverage": coverage}
    return {"data": validated, "coverage": coverage}