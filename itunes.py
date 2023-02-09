
import requests

def main():

    variable = variables()

    response = requests.get(f"https://itunes.apple.com/search?entity=song&limit={variable[1]}&term={variable[0]}")

    o = response.json()
    for result in o["results"]:
        print(result["trackName"])

def variables():
    artist = input("Type name of singer/ band: ")
    songs = input("How many songs you want to filter: ")
    return (artist, songs)

if __name__ == '__main__':
    main()