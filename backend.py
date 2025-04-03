from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Initialize FastAPI app
app = FastAPI()

# Load CodeLlama Model
MODEL_PATH = "./saved_codellema"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)

class CodeRequest(BaseModel):
    code_snippet: str

def detect_and_fix_bug(code_snippet):
    """
    Detects and fixes bugs in a given code snippet using CodeLlama.
    """
    prompt = f"""
    ### Buggy Code:
    {code_snippet}

    ### Task:
    1. Identify if there is an error in the code.
    2. Highlight the exact line where the error occurs.
    3. Provide a corrected version of the code.

    ### Analysis:
    """
    # Tokenize input
    inputs = tokenizer(prompt, return_tensors="pt").to("cpu")
    # Generate output
    output = model.generate(
        **inputs,
        max_length=512,
        temperature=0.2,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

    # Decode output
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

@app.post("/analyze")
async def analyze_code(request: CodeRequest):
    """API endpoint to analyze and fix code."""
    result = detect_and_fix_bug(request.code_snippet)
    return {"analysis": result}

