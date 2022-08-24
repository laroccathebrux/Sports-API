import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

def main():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('rohanrao/formula-1-world-championship-1950-2020', path='csv/f1', unzip=True)

if __name__ == '__main__':
    main()
