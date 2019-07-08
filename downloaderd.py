import os
from datetime import datetime, timedelta

path = "./gefs/"

def main():

    f = open("downloaderstatus", 'r')
    if f.readline() == "Running":
        print("Downloader process already running, quitting")
        return
    f.close()
    f = open("downloaderstatus", 'w')
    if not __name__ == "__main__":
        f.write("Running")
    f.close()

    try:
        os.mkdir("gefs")
    except FileExistsError:
        pass
            
    now = datetime.utcnow()
    timestamp = datetime(now.year, now.month, now.day, int(now.hour / 6) * 6) - timedelta(hours=6)
    while True:
        command = "python3 downloader.py " + str(timestamp.year) + " " + str(timestamp.month) + " " + str(timestamp.day) + " " + str(timestamp.hour)
        
        g = open("serverstatus", "w")
        g.write("Data refreshing. Sims may be slower than usual.")
        g.close()
        
        while True:
            try: 
                os.system(command)
                break
            except:
                print("Error, restarting downloader process")
        f = open("whichgefs", "w")
        f.write(timestamp.strftime("%Y%m%d%H"))
        f.close()

        g = open("serverstatus", "w")
        g.write("Ready")
        g.close()

        prev_timestamp = timestamp - timedelta(hours=6)
        os.system("rm " + path + prev_timestamp.strftime("%Y%m%d%H") + "*")
        timestamp = timestamp + timedelta(hours=6)

if __name__ == "__main__":
    main()