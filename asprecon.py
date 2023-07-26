import requests, argparse, sys, time, urllib3
from termcolor import colored

# Disable warning about SSL, comment if needed
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# global vars
delay = 0


file = open("/usr/share/seclists/Discovery/Web-Content/iis-systemweb.txt", "r")
versions = file.readlines()
file.close()


def CheckDirectory(target):
    try:
        print("\nChecking if target is vulnerable.\n")
        r = requests.get(url="%s/aspnet_client/" % target, verify=False)

        if str(r.status_code) == "403" or str(r.status_code) == "403.14":
            r = requests.get(url="%s/aspnet_clien/" % target, verify=False)

            if str(r.status_code) == "403" or str(r.status_code) == "403.14":
                print(colored("Target is likely not vulnerable.\n", "red"))
                return False

            else:
                print(colored("Target is likely vulnerable.", "green"))
                return True
        
        else:
            print(colored("Target is likely not vulnerable.\n", "red"))
            return False
        
    except Exception as e:
        print(e)
        exit(1)

def BruteForce(target):
    for version in versions:
        version = requests.utils.quote(version.strip())

        if delay <= 0:
            a = requests.get(url="%s/aspnet_client/system_web/%s/" % (target,str(version)), verify=False)
            
            if str(a.status_code) == "403" or str(a.status_code) == "403.14":
                print(colored("Asp.Net version: " + version.replace("_","."), "yellow"))
                        
            else:
                continue
        else:
            time.sleep(delay)
            a = requests.get(url="%s/aspnet_client/system_web/%s/" % (target,str(version)), verify=False)
            if str(a.status_code) == "403" or str(a.status_code) == "403.14":
                print(colored("Asp.Net version: " + version.replace("_","."), "yellow"))
                        
            else:
                continue

def main():

    global delay

    parser = argparse.ArgumentParser(epilog="e.g. python3 asprecon -t http/s://127.0.0.1:80 -d 1",)
    parser.add_argument("-t", "--target", metavar='', help="Target to scan (ip/domain)", required=True)
    parser.add_argument("-d", "--delay",metavar='', type=int, help="Time delay each scan per second(s)")
                        
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

