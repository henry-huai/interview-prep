from typing import Dict, Set


REQUIRED_FIELDS: set[str] = {"age", "income", "credit_score"}


def validate_input(data: dict) -> dict[str, float]:
    """
    Rules:
    - All required fields must be present
    - All values must be numeric
    - All values must be non-negative
    - All values are normalized to float
    """
    # Check input type
    if not isinstance(data, dict):
        raise ValueError("Input data must be a dictionary")

    # Check for missing required fields
    missing_fields = REQUIRED_FIELDS - data.keys()
    if missing_fields:
        raise ValueError("Missing required fields: {missing_fields}")
    
    for value in data.values():
        if not isinstance(value, (int, float)):
            raise TypeError("All values must be numeric")
    
    for value in data.values():
        if value < 0:
            raise ValueError("All values must be non-negative")

    for value in data.values():
        try:
            value = float(value)
        except(ValueError):
            raise ValueError('All values are normalized to float')
    return data


if __name__ == "__main__":
    # Manual sanity check
    valid_input = {
        "age": 30,
        "income": 70000,
        "credit_score": 720
    }

    print(validate_input(valid_input))
