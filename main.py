import os

from pyfiglet import Figlet
from pytube import YouTube
from pytube.cli import on_progress


outputPath = 'out'



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

    for args in command:
        if args == '-a' or args == '-audio': # audio flag check
            youtubeURL.streams.get_audio_only().download(outputPath)
        elif args == '-hr' or args == '-highres':
            youtubeURL.streams.get_highest_resolution().download(outputPath)
        else:
            youtubeURL.streams.get_by_itag(22).download(outputPath)

    print(f'{youtubeURL.title} downloaded to {os.path.abspath(outputPath)}')

    main()


def clear():
    os.system('cls')

    main()


def unknown(userInput: str):
    print(f'{userInput} is not a recognized command!')

    help()


def help():
    print('------------')
    print (' help page ')
    print('------------')
    print('\n')
    print(' ex: <command> (params) [options]')
    print('     download https://www.youtube.com/watch?v=5X3TXa8TMgo -audio')
    print('\n')
    print(' help                    : Displays a list of commands, their parameters and purpose.')
    print(' download (URL) [-audio] [-highres]: Downloads video through given URL')
    print('       -audio   : Downloads only audio')
    print('       -highres : Downloads highest resolution available')

    main()


## input
def main():
    thisPath = os.path.abspath(__file__)

    userInput = input(f'{thisPath}> ')


    if userInput.startswith('download'):
        download(userInput)
    elif userInput.startswith('help'):
        help()
    elif userInput.startswith('clear') | userInput.startswith('cls'):
        clear()
    else:
        unknown(userInput)


if __name__ == '__main__':
    main()