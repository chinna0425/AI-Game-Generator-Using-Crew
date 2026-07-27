import os
import re

# Output Directory

OUTPUT_DIR = "generated"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Helper Functions

def get_final_output(result):
    """
    Extract the final text from CrewOutput.
    Supports multiple CrewAI versions.
    """

    if hasattr(result, "raw") and result.raw:
        return result.raw

    return str(result)


def extract_python_code(text):
    """
    Extract Python code from the model response.
    """
    
    # Pattern 1
    # ```python
    # ...
    # ```
    
    match = re.search(
        r"```(?:python)?\s*(.*?)```",
        text,
        re.DOTALL | re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    
    # Pattern 2
    # Python Code
    # -----------
    # code...
    # Requirements

    match = re.search(
        r"Python Code\s*-*\s*(.*?)Requirements",
        text,
        re.DOTALL | re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    return ""

def extract_section(text, start, end=None):
    """
    Extract a section between two headings.
    """

    if end:
        pattern = rf"{start}\s*-*\s*(.*?){end}"

    else:
        pattern = rf"{start}\s*-*\s*(.*)"

    match = re.search(
        pattern,
        text,
        re.DOTALL | re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    return ""

# Main Parser

def parse_output(result):
    """
    Parse CrewAI output.
    """

    final_output = get_final_output(result)

    # Save complete response 

    txt_path = os.path.join(
        OUTPUT_DIR,
        "generated_game.txt"
    )

    with open(txt_path, "w", encoding="utf-8") as file:
        file.write(final_output)

    # Extract Sections    

    game_review = extract_section(
        final_output,
        "Game Review",
        "Python Code"
    )

    requirements = extract_section(
        final_output,
        "Requirements"
    )

    python_code = extract_python_code(
        final_output
    )

    # Save Python File

    py_path = os.path.join(
        OUTPUT_DIR,
        "generated_game.py"
    )

    if python_code:

        with open(py_path, "w", encoding="utf-8") as file:
            file.write(python_code)

        file_path = py_path

    else:

        file_path = None

    
    # Return

    return {

        "game_review": game_review,

        "python_code": python_code,

        "requirements": requirements,

        "file_path": file_path,

        "full_output": final_output

    }