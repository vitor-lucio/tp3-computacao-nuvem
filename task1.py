def handler(input: dict, context: object) -> dict[str, any]:
    print(input)
    return {"test": 34}

print(handler({"test": "testing"}, {}))