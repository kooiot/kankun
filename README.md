# kankun
>cgi script controls kankun wifi smart plug

### Install Scripts
> SSH to your device, make folder cgi-bin
>> mkdir /www/cgi-bin
> Copy file to cgi-bin folder by using scp


### Control the switch:
> http://<your device ip>/cgi-bin/relay.cgi?on
> http://<your device ip>/cgi-bin/relay.cgi?off
> http://<your device ip>/cgi-bin/relay.cgi?state

### There are also:
> timing.cgi?online <p>
> timing.cgi?offline
> light.cgi?state
> light.cgi?on
> light.cgi?off
> power.cgi
