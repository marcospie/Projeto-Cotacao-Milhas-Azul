
import requests


def get_token_azul():

    subscription_key = "0fc6ff296ef2431bb106504c92dd227c"
    url = "https://b2c-api.voeazul.com.br/authentication/api/authentication/v1/token"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-ZA,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,en-GB;q=0.6,en-US;q=0.5",
        "Content-Length": "0",
        "Culture": "pt-BR",
        "Device": "novosite",
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Origin": "https://www.voeazul.com.br",
        "Referer": "https://www.voeazul.com.br/",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    response = requests.post(url, headers=headers)
    data = response.json()
    return data["data"]