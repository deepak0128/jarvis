import multiprocessing
import subprocess

def startJarvis():
    print("Process 1 is running.")
    from main import start
    start()

def listenHotword():
    print("Process 2 is running.")
    from engine.features import hotword
    hotword()          

def runDeviceBat():
    print("Running device.bat...")
    subprocess.call([r'device.bat'])

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=startJarvis)
    p2 = multiprocessing.Process(target=listenHotword)
    p3 = multiprocessing.Process(target=runDeviceBat)
    
    p1.start()
    p3.start()
    p2.start()

    p1.join()
    
    if p2.is_alive():
        p2.terminate()
        p2.join()

    p3.join()  # Wait for the batch file process to finish
    
    print("System stop")
