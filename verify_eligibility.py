import requests

class EligibilityClient:
    def __init__(self,base_url):
        self.base_url = base_url
    
    def verify(self,carrier_name, member_id, full_name, dob):
        url = f"{self.base_url}/verify"
        payload = {
            "carrier_name": carrier_name,
            "member_id": member_id,
            "full_name": full_name,
            "dob": dob
        }
        response = requests.post(url, json=payload)
        return response.json()