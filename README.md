# Eligibility Verification SDK

## Overview

This project provides a Python SDK to interact with an eligibility verification API. The SDK is generated from the `eligibility_api.yaml` OpenAPI specification and includes methods to verify patient eligibility via the `/verify` endpoint.

## Setup

1. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Generate SDK**:

   ```bash
   python generate_sdk.py
   ```

3. **Run the API Server** (for live testing):

   - If you have a local API server, ensure it is running at `http://localhost:8000`

4. **Run Tests**:
   ```bash
   pytest
   ```

## Usage

Example usage of the `EligibilityClient` class:

```python
from verify_eligibility import EligibilityClient

client = EligibilityClient(base_url="http://localhost:8000")
response = client.verify(
    carrier_name="Test Carrier",
    member_id="111111",
    full_name="Erol Kaan",
    dob="2023-02-03"
)
print(response)
```

