import requests

with open("mock.csv", "rb") as f:
    response = requests.post(
        "https://llm-analyst-backend.onrender.com/analyze",
        files={"file": f}  # must be multipart/form-data
    )

print(response.status_code)
print(response.json())
