# asprecon
This tool is used for active ASP.NET reconnaissance.  The ``usr/share/seclists/Discovery/Web-Content/iis-systemweb.txt`` wordlist is used as payloads.
If the target responds with a status code 403 against any of the versions, the web server likely supports that aspnet version. 

## Usage:
```
python3 asprecon.py -t/--target <ip/domain>
```

### Time delay
```
python3 asprecon.py -t/--target <ip/domain> -d/--delay <int>
```
