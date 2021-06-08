import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config
import time
from selenium import webdriver
import os, glob
import pycountry
import pandas as pd


class SpotifyAPI:
    def __init__(self):
        client_credentials_manager = SpotifyClientCredentials(
            client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET
        )
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def download_all_charts():
    SUPPORTED_REGIONS = [
        "us",
        "gb",
        "ae",
        "ar",
        "at",
        "au",
        "be",
        "bg",
        "bo",
        "br",
        "ca",
        "ch",
        "cl",
        "co",
        "cr",
        "cy",
        "cz",
        "de",
        "dk",
        "do",
        "ec",
        "ee",
        "eg",
        "es",
        "fi",
        "fr",
        "gr",
        "gt",
        "hk",
        "hn",
        "hu",
        "id",
        "ie",
        "il",
        "in",
        "is",
        "it",
        "jp",
        "kr",
        "lt",
        "lu",
        "lv",
        "ma",
        "mx",
        "my",
        "ni",
        "nl",
        "no",
        "nz",
        "pa",
        "pe",
        "ph",
        "pl",
        "pt",
        "py",
        "ro",
        "ru",
        "sa",
        "se",
        "sg",
        "sk",
        "sv",
        "th",
        "tr",
        "tw",
        "ua",
        "uy",
        "vn",
        "za",
    ]

    WEEKLY_CHARTS_DATES = [
        "2021-05-28--2021-06-04",
        "2021-05-21--2021-05-28",
        "2021-05-14--2021-05-21",
        "2021-05-07--2021-05-14",
        "2021-04-30--2021-05-07",
        "2021-04-23--2021-04-30",
        "2021-04-16--2021-04-23",
        "2021-04-09--2021-04-16",
        "2021-04-02--2021-04-09",
        "2021-03-26--2021-04-02",
        "2021-03-19--2021-03-26",
        "2021-03-12--2021-03-19",
        "2021-03-05--2021-03-12",
        "2021-02-26--2021-03-05",
        "2021-02-19--2021-02-26",
        "2021-02-12--2021-02-19",
        "2021-02-05--2021-02-12",
        "2021-01-29--2021-02-05",
        "2021-01-22--2021-01-29",
        "2021-01-15--2021-01-22",
        "2021-01-08--2021-01-15",
        "2021-01-01--2021-01-08",
        "2020-12-25--2021-01-01",
        "2020-12-18--2020-12-25",
        "2020-12-11--2020-12-18",
        "2020-12-04--2020-12-11",
        "2020-11-27--2020-12-04",
        "2020-11-20--2020-11-27",
        "2020-11-13--2020-11-20",
        "2020-11-06--2020-11-13",
        "2020-10-30--2020-11-06",
        "2020-10-23--2020-10-30",
        "2020-10-16--2020-10-23",
        "2020-10-09--2020-10-16",
        "2020-10-02--2020-10-09",
        "2020-09-25--2020-10-02",
        "2020-09-18--2020-09-25",
        "2020-09-11--2020-09-18",
        "2020-09-04--2020-09-11",
        "2020-08-28--2020-09-04",
        "2020-08-21--2020-08-28",
        "2020-08-14--2020-08-21",
        "2020-08-07--2020-08-14",
        "2020-07-31--2020-08-07",
        "2020-07-24--2020-07-31",
        "2020-07-17--2020-07-24",
        "2020-07-10--2020-07-17",
        "2020-07-03--2020-07-10",
        "2020-06-26--2020-07-03",
        "2020-06-19--2020-06-26",
        "2020-06-12--2020-06-19",
        "2020-06-05--2020-06-12",
        "2020-05-29--2020-06-05",
        "2020-05-22--2020-05-29",
        "2020-05-15--2020-05-22",
        "2020-05-08--2020-05-15",
        "2020-05-01--2020-05-08",
        "2020-04-24--2020-05-01",
        "2020-04-17--2020-04-24",
        "2020-04-10--2020-04-17",
        "2020-04-03--2020-04-10",
        "2020-03-27--2020-04-03",
        "2020-03-20--2020-03-27",
        "2020-03-13--2020-03-20",
        "2020-03-06--2020-03-13",
        "2020-02-28--2020-03-06",
        "2020-02-21--2020-02-28",
        "2020-02-14--2020-02-21",
        "2020-02-07--2020-02-14",
        "2020-01-31--2020-02-07",
        "2020-01-24--2020-01-31",
        "2020-01-17--2020-01-24",
        "2020-01-10--2020-01-17",
        "2020-01-03--2020-01-10",
        "2019-12-27--2020-01-03",
        "2019-12-20--2019-12-27",
        "2019-12-13--2019-12-20",
        "2019-12-06--2019-12-13",
        "2019-11-29--2019-12-06",
        "2019-11-22--2019-11-29",
        "2019-11-15--2019-11-22",
        "2019-11-08--2019-11-15",
        "2019-11-01--2019-11-08",
        "2019-10-25--2019-11-01",
        "2019-10-18--2019-10-25",
        "2019-10-11--2019-10-18",
        "2019-10-04--2019-10-11",
        "2019-09-27--2019-10-04",
        "2019-09-20--2019-09-27",
        "2019-09-13--2019-09-20",
        "2019-09-06--2019-09-13",
        "2019-08-30--2019-09-06",
        "2019-08-23--2019-08-30",
        "2019-08-16--2019-08-23",
        "2019-08-09--2019-08-16",
        "2019-08-02--2019-08-09",
        "2019-07-26--2019-08-02",
        "2019-07-19--2019-07-26",
        "2019-07-12--2019-07-19",
        "2019-07-05--2019-07-12",
        "2019-06-28--2019-07-05",
        "2019-06-21--2019-06-28",
        "2019-06-14--2019-06-21",
        "2019-06-07--2019-06-14",
        "2019-05-31--2019-06-07",
        "2019-05-24--2019-05-31",
        "2019-05-17--2019-05-24",
        "2019-05-10--2019-05-17",
        "2019-05-03--2019-05-10",
        "2019-04-26--2019-05-03",
        "2019-04-19--2019-04-26",
        "2019-04-12--2019-04-19",
        "2019-04-05--2019-04-12",
        "2019-03-29--2019-04-05",
        "2019-03-22--2019-03-29",
        "2019-03-15--2019-03-22",
        "2019-03-08--2019-03-15",
        "2019-03-01--2019-03-08",
        "2019-02-22--2019-03-01",
        "2019-02-15--2019-02-22",
        "2019-02-08--2019-02-15",
        "2019-02-01--2019-02-08",
        "2019-01-25--2019-02-01",
        "2019-01-18--2019-01-25",
        "2019-01-11--2019-01-18",
        "2019-01-04--2019-01-11",
        "2018-12-28--2019-01-04",
        "2018-12-21--2018-12-28",
        "2018-12-14--2018-12-21",
        "2018-12-07--2018-12-14",
        "2018-11-30--2018-12-07",
        "2018-11-23--2018-11-30",
        "2018-11-16--2018-11-23",
        "2018-11-09--2018-11-16",
        "2018-11-02--2018-11-09",
        "2018-10-26--2018-11-02",
        "2018-10-19--2018-10-26",
        "2018-10-12--2018-10-19",
        "2018-10-05--2018-10-12",
        "2018-09-28--2018-10-05",
        "2018-09-21--2018-09-28",
        "2018-09-14--2018-09-21",
        "2018-09-07--2018-09-14",
        "2018-08-31--2018-09-07",
        "2018-08-24--2018-08-31",
        "2018-08-17--2018-08-24",
        "2018-08-10--2018-08-17",
        "2018-08-03--2018-08-10",
        "2018-07-27--2018-08-03",
        "2018-07-20--2018-07-27",
        "2018-07-13--2018-07-20",
        "2018-07-06--2018-07-13",
        "2018-06-29--2018-07-06",
        "2018-06-22--2018-06-29",
        "2018-06-15--2018-06-22",
        "2018-06-08--2018-06-15",
        "2018-06-01--2018-06-08",
        "2018-05-25--2018-06-01",
        "2018-05-18--2018-05-25",
        "2018-05-11--2018-05-18",
        "2018-05-04--2018-05-11",
        "2018-04-27--2018-05-04",
        "2018-04-20--2018-04-27",
        "2018-04-13--2018-04-20",
        "2018-04-06--2018-04-13",
        "2018-03-30--2018-04-06",
        "2018-03-23--2018-03-30",
        "2018-03-16--2018-03-23",
        "2018-03-09--2018-03-16",
    ]
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "/Users/shakedzrihen/Documents/סדנה במדעי הנתונים/finalProject/dataset"}
    chromeOptions.add_experimental_option("prefs", prefs)
    chromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
    chromeOptions.add_argument("start-maximized")
    chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
    chromeOptions.add_argument("disable-infobars")
    chromeOptions.add_argument("--disable-extensions")
    chromedriver = "./chromedriver"
    driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)

    for week in WEEKLY_CHARTS_DATES[1:]:
        for region in SUPPORTED_REGIONS:
            try:
                driver.get(f"https://spotifycharts.com/regional/{region}/weekly/{week}")
                download_button = driver.find_element_by_class_name("header-csv")
                download_button.click()
                time.sleep(1)
            except:
                pass


def format_spotify_csv_charts():
    # Take dates and country from filename
    # Append date and country as new 2 columns

    for filename in os.listdir("./dataset"):
        try:
            country = filename.split("-")[1]
            country_name = pycountry.countries.get(alpha_2=country).name
            dates = filename.split(f"regional-{country}-weekly-")[1].split(".csv")[0].replace(" (1)", "")
            csv_input = pd.read_csv(f"./dataset/{filename}")
            new_header = csv_input.iloc[0]
            csv_input = csv_input[1:]
            csv_input.columns = new_header
            csv_input["country"] = country_name
            csv_input["dates"] = dates
            csv_input.to_csv(f"./formattedDatasetNew/{filename}", index=False)
            print(f"Finish processing: {filename}")
        except:
            pass


def merge_charts_csvs():
    # merge all csv to 1 file

    path = "./formattedDatasetNew"

    all_files = glob.glob(os.path.join(path, "*.csv"))

    all_df = []
    for f in all_files:
        df = pd.read_csv(f, sep=",")
        all_df.append(df)

    merged_df = pd.concat(all_df, ignore_index=True, sort=True)
    merged_df.to_csv("./mergedDataset")


def get_uniqe_songs_data():
    api = SpotifyAPI()
    music_keys = {
        0: "C",
        1: "C#",
        2: "D",
        3: "D#",
        4: "E",
        5: "F",
        6: "F#",
        7: "G",
        8: "G#",
        9: "A",
        10: "A#",
        11: "B",
    }
    csv_input = pd.read_csv(f"./mergedDataset.csv")
    uniqe_songs_ids = csv_input["URL"].unique()
    print(f"Going to process {len(uniqe_songs_ids)} uniqe songs")
    empty_dataframe = pd.read_csv(f"./songsData.csv")
    songs_to_write = 0
    for song in uniqe_songs_ids[801:]:
        try:
            row = {}
            track_id = song.rsplit("/", 1)[-1]
            track_data = api.sp.audio_features(tracks=[track_id])[0]
            row["URL"] = song
            row["danceability"] = track_data["danceability"]
            row["energy"] = track_data["energy"]
            row["key"] = music_keys.get(track_data["key"], "null")
            row["loudness"] = track_data["loudness"]
            row["mode"] = track_data["mode"]
            row["speechiness"] = track_data["speechiness"]
            row["acousticness"] = track_data["acousticness"]
            row["instrumentalness"] = track_data["instrumentalness"]
            row["liveness"] = track_data["liveness"]
            row["valence"] = track_data["valence"]
            row["tempo"] = track_data["tempo"]
            row["duration_ms"] = track_data["duration_ms"]
            empty_dataframe = empty_dataframe.append(row, ignore_index=True)
            print(f"Calculated row number: {songs_to_write}")
            songs_to_write += 1
            if songs_to_write % 100 == 0:
                print(f"Write next 100 songs (total: {songs_to_write})...")
                empty_dataframe.to_csv(f"./songsData.csv", index=False)
        except Exception as e:
            print(f"Got excepetion: {e}")
            pass
    empty_dataframe.to_csv(f"./songsData.csv", index=False)


def merge_uniqu_songs_with_all_charts():
    songs_df = pd.read_csv("./songsData.csv")
    charts_df = pd.read_csv("mergedDataset.csv")
    merged_df = charts_df.merge(songs_df, on="URL")
    merged_df.to_csv("./fullDataset.csv")


def init_dataset_workflow():
    download_all_charts()
    format_spotify_csv_charts()
    merge_charts_csvs()
    get_uniqe_songs_data()
    merge_uniqu_songs_with_all_charts()
