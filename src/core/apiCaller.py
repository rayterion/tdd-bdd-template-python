import requests

dbBaseURL = "https://www.example.com"
class ApiCaller:
    def getApiRandomNumbers(self):
        try:
            res = requests.get(dbBaseURL + "/api/randomNumbers")
            return res.json()
        except Exception:
            return {"status_code": 400} 
    