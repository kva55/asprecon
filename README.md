# asprecon
This tool is used for active ASP.NET reconnaissance.  The ``/usr/share/seclists/Discovery/Web-Content/iis-systemweb.txt`` wordlist is used for payloads.
If the target responds with a status code 403 against any of the versions, the web server likely supports that aspnet version. 

## Usage:
```
python3 asprecon.py -t/--target <http/s://target>
```

### Time delay
```
python3 asprecon.py -t/--target <http/s://target> -d/--delay <int>
```

<div align="center"">

![asprecon](https://github.com/kva55/asprecon/assets/60018788/c8e6bce4-2112-498a-8903-64bc134776d4)

</div>
