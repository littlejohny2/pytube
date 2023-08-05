import os

from pyfiglet import Figlet
from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress


outputPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'out')



## pretty intro ##
figlet = Figlet(font='slant')
print( figlet.renderText('python video download') )


## commands
def download(userInput: str):
    command = userInput.split()

    try:
        youtubeURL = YouTube(command[1], on_progress_callback=on_progress)
    except:
        print('URL INVALID')
        return main()

    for args in command[2:]:
        if args == '-a' or args == '-audio': # audio flag check
            print(f'\n  downloading {youtubeURL.title}...')
            youtubeURL.streams.get_audio_only().download(outputPath)
        elif args == '-hr' or args == '-highres':
            print(f'\n  downloading {youtubeURL.title}...')
            youtubeURL.streams.get_highest_resolution().download(outputPath)
        else:
            print(f'\n  downloading {youtubeURL.title}...')
            youtubeURL.streams.get_by_itag(22).download(outputPath)

    print(f'\n{youtubeURL.title} downloaded to {os.path.abspath(outputPath)}')

    main()


def playlist(userInput: str):
    command = userInput.split()

    try:
        playlistURL = Playlist(command[1])
    except:
        print('URL INVALID')
        return main()
    
    for args in command[2:]:
        if args == '-a' or args == '-audio':

            for video in playlistURL.videos:
                print(f'\n  downloading {video.title}...')
                video.register_on_progress_callback(on_progress)
                video.streams.get_audio_only().download(outputPath)

        elif args == '-hr' or args == '-highres':

            for video in playlistURL.videos:
                print(f'\n  downloading {video.title}')
                video.register_on_progress_callback(on_progress)
                video.streams.get_highest_resolution().download(outputPath)

        else:

            for video in playlistURL.videos:
                print(f'\n  downloading {video.title}')
                video.register_on_progress_callback(on_progress)
                video.streams.get_by_itag(22).download(outputPath)

    print(f'\n{playlistURL.title} downloaded to {os.path.abspath(outputPath)}')

    main()


def clean(userInput: str):
    command = userInput.split()
    
    for args in command[1:]:
        if args == '-y' or args == '-yes': # -yes option bypasses prompt
            for files in os.listdir(outputPath):
                print(f' removing {files}')
                os.remove(os.path.join(outputPath, files))

            print(f'{outputPath} cleaned')

            return main()

    yesNoInput = input('are you sure you want to delete all files in the out directory? [y/N]')

    if yesNoInput == 'y' or yesNoInput == 'Y' or yesNoInput == 'yes' or yesNoInput == 'YES':
        for files in os.listdir(outputPath):
            print(f' removing {files}')
            os.remove(os.path.join(outputPath, files))

        print(f'{outputPath} cleaned')

        return main()
    else:

        return main()



def clear():
    os.system('cls')

    main()


def unknown(userInput: str):
    print(f'{userInput} is not a recognized command!')

    help()


def help():
    print('\n')
    print('------------')
    print('  help page ')
    print('------------')
    print('\n')
    print(' ex: <command> (params) [options]')
    print('     download https://www.youtube.com/watch?v=5X3TXa8TMgo -audio')
    print('\n')
    print(' help                              : Displays a list of commands, their parameters and purpose.')
    print(' clean [-yes]                      : Deletes all files found in the output directory.')
    print('       -yes   : Bypasses y/N prompt with yes')
    print(' download (URL) [-audio] [-highres]: Downloads video through given URL')
    print('       -audio   : Downloads only audio')
    print('       -highres : Downloads highest resolution available')
    print(' playlist (URL) [-audio] [-highres]: Downloads video from a playlist through given URL')
    print('       -audio   : Downloads only audio')
    print('       -highres : Downloads highest resolution available')
    print('\n')


    main()


## input
def main():
    thisPath = os.path.abspath(__file__)

    userInput = input(f'{thisPath}> ')


    if userInput.startswith('download'):
        download(userInput)
    elif userInput.startswith('playlist'):
        playlist(userInput)
    elif userInput.startswith('clean'):
        clean(userInput)
    elif userInput.startswith('help'):
        help()
    elif userInput.startswith('clear') | userInput.startswith('cls'):
        clear()
    else:
        unknown(userInput)


if __name__ == '__main__':
    main()