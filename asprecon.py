import requests, argparse, sys


file = open("/usr/share/seclists/Discovery/Web-Content/iis-systemweb.txt", "r")
versions = file.readlines()
file.close()



def CheckDirectory(target):
    print("Checking if target is vulnerable.")
    r = requests.get(url="http://%s/aspnet_client/" % target)
    if str(r.status_code) == "403" or str(r.status_code) == "403.14":
        print("Target is likely vulnerable.")
        return True
    
    else:
        print("Target is likely not vulnerable.")
        return False

def BruteForce(target):
    for version in versions:
        version = requests.utils.quote(version.strip())
        a = requests.get(url="http://%s/aspnet_client/system_web/%s/" % (target,str(version)))
        
        if str(a.status_code) == "403" or str(a.status_code) == "403.14":
            print("Asp.Net version: " + version.replace("_","."))
                    
        else:
            continue

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", help="target to scan", required=True)
    args = parser.parse_args()

    target = args.target
              
    var = CheckDirectory(target)
    ans = input("Do you still want to proceed with the scan? (Y/N) ")

    if str(ans).lower() == "y" or str(ans).lower() == "yes":
        BruteForce(target)
    else:
        exit(0)

if __name__ == "__main__":
    main()
