import app as application

def handler(event):
    with application.app.test_client() as client:
        response = client.post("/run", json=event)
        return response.get_json()