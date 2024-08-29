import subprocess
import logging

def generate_sdk():
    
    url = "eligibility_api.yaml"
    subprocess.run([
        "openapi-python-client", "generate", "--path", url
    ])
    logging.info(f"Generated SDK")

if __name__ == "__main__":
    generate_sdk()


