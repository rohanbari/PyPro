# YouTube Video Downloader

import pytube

DESKTOP_LOCATION = '/home/rohan/Desktop'


def downloader(link, name):
    """Downloads the relevant YouTube video with the link.

    Args:
        link (string): Video link
        name (string): Downloaded file name
    """

    url = pytube.YouTube(link)
    video = url.streams.get_lowest_resolution()
    video.download(output_path=DESKTOP_LOCATION, filename=name)

    print('Download successful!')


file_link = input('Enter the video link here: ')
file_name = input('Enter the file name: ')

downloader(file_link, file_name)

print('The downloaded file has been saved on your Desktop.')
