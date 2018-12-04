from google_drive_downloader import GoogleDriveDownloader as gdd
import argparse


gdd.download_file_from_google_drive(fileid='1iU_RLosQYPmKC__pQ4QY_e4OziDJ_iZJ',
                                    dest_path='data/ADEChallengeData2016.zip',
                                    unzip=True
                                    )
gdd.download_file_from_google_drive(fileid='1ryg9efSh9barf6lMJ0xB78UM9orhJN7B',
                                    dest_path='model/ade20k.zip',
                                    unzip=True)
