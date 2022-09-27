import pytube

#save in current directory
download_location = './'

#ask user to enter url for youtube video
video_url = input('Enter url: ')

#Create an instance of youtube video
video_instance = pytube.YouTube(video_url)

stream = video_instance.streams.get_highest_resolution()

#download 
stream.download()