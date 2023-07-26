# asprecon
This tool is used for active ASP.NET reconnaissance.  The ``/usr/share/seclists/Discovery/Web-Content/iis-systemweb.txt`` wordlist is used as payloads.
If the target responds with a status code 403 against any of the versions, the web server likely supports that aspnet version. 

## Usage:
```
python3 asprecon.py -t/--target <ip/domain>
```

### Time delay
```
python3 asprecon.py -t/--target <ip/domain> -d/--delay <int>
```

<div align="center"">

![asprecon](https://github.com/kva55/asprecon/assets/60018788/f72f973f-680b-43fe-93d6-6d3780fe7bab)

</div>
