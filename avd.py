import subprocess
import os


def main():
    def parse_input():
        selection = input('Input: ')
        if (selection.isnumeric()):
            index = int(selection)
            if (0 <= index < len(avds)):
                start_avd(avds[index])
            else:
                parse_input()
        else:
            if (selection.lower() == 'q'):
                exit(0)
            else:
                parse_input()

    def start_avd(name):
        devnull = open(os.devnull, 'wb')
        subprocess.Popen([path + 'emulator', '@{}'.format(name)], stdout=devnull, stderr=devnull)

    path = os.environ['ANDROID_HOME'] + '/tools/'
    avd_manager = subprocess.Popen([path + 'bin/avdmanager', 'list', 'avd'], stdout=subprocess.PIPE)
    awk = subprocess.Popen(['awk', '/Name/ { print $2 }'], stdin=avd_manager.stdout, stdout=subprocess.PIPE)
    avds = [x.decode('UTF-8').strip('\n') for x in awk.stdout]
    print('Select AVD to run')
    print('-' * 20)
    for (i, avd) in enumerate(avds):
        print('({}) - {}'.format(i, avd))
    print('(q) - Quit')
    print('-' * 20)
    parse_input()


if __name__ == '__main__':
    main()
