import requests

dbBaseURL = "https://www.example.com"
class ApiCaller:
    def getApiRandomNumbers(self):
        res = requests.get(dbBaseURL + "/api/randomNumbers")
        return res.json()
    