import math, time, _thread, sys, os
from schedule import schedule
from sun import sun
from wind import wind
from battery import battery
from panels import panels

def WaitForKeyPress(L):
    ''' Wait for a key press on the console and return it. '''
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()
        L.append(None)
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
            L.append(None)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result


def CreateBattery(battery):
    ''' Create the empty battery'''
    myBattery = Battery(0.0)
    return myBattery.level
    print (myBattery.level)

def CreatePanel(panel):
    ''' Create a panel'''
    myPanel = Panel(a, s, w)
    return myPanel
    print (myPanel.a)

def Simulate():
    L = []
    timestep = 0
    _thread.start_new_thread(WaitForKeyPress, (L,))

    while 1:
        time.sleep(1) # delay for 1 second.
        if L: break

        print ("The timestep of the simulation is: {}".format(str(timestep)))
        timestep+=1

        for s in schedule:
            s.whatmonth()
            print(schedule.name)
            return

#Remember this method gets executed first since its our 'main'
def main():

    #Make some vegtables
    battery = []
    CreateBattery(battery)

    print("\nPress Any key to quit simulation...\n")
    Simulate()



if __name__ == "__main__":
    main()