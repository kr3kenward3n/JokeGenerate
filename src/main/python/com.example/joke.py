import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"

    try:
        response = requests.get(url)
        response.raise_for_status()

        joke_data = response.json()

        if joke_data['type'] == 'single':
            return joke_data['joke']
        else:
            return f"{joke_data['setup']} ... {joke_data['delivery']}"

    except requests.exceptions.RequestException as e:
        return f"Ошибка при получении шутки: {e}"


if __name__ == "__main__":
    print("Вот ваша шутка:")
    print(get_joke())