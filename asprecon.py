import requests, argparse, sys, time
from termcolor import colored


# global vars
delay = 0


file = open("/usr/share/seclists/Discovery/Web-Content/iis-systemweb.txt", "r")
versions = file.readlines()
file.close()


def CheckDirectory(target):
    print("\nChecking if target is vulnerable.\n")
    r = requests.get(url="http://%s/aspnet_client/" % target)
    if str(r.status_code) == "403" or str(r.status_code) == "403.14":
        print(colored("Target is likely vulnerable.", "green"))
        return True
    
    else:
        print("Target is likely not vulnerable.\n")
        return False

def BruteForce(target):
    for version in versions:
        version = requests.utils.quote(version.strip())

        if delay <= 0:
            a = requests.get(url="http://%s/aspnet_client/system_web/%s/" % (target,str(version)))
            
            if str(a.status_code) == "403" or str(a.status_code) == "403.14":
                print(colored("Asp.Net version: " + version.replace("_","."), "yellow"))
                        
            else:
                continue
        else:
            time.sleep(delay)
            a = requests.get(url="http://%s/aspnet_client/system_web/%s/" % (target,str(version)))
            if str(a.status_code) == "403" or str(a.status_code) == "403.14":
                print(colored("Asp.Net version: " + version.replace("_","."), "yellow"))
                        
            else:
                continue

def main():

    global delay

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", help="Target to scan (ip/domain)", required=True)
    parser.add_argument("-d", "--delay",type=int, help="Time delay each scan per second(s)")
    args = parser.parse_args()

    target = args.target
    if args.delay:
        delay = args.delay
              
    var = CheckDirectory(target)
    ans = input("Do you still want to proceed with the scan? (Y/N) ")

    if str(ans).lower() == "y" or str(ans).lower() == "yes":
        BruteForce(target)
    else:
        exit(0)

if __name__ == "__main__":
    main()
