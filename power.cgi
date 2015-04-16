#!/bin/sh

echo "Content-Type: text/plain"
echo "Cache-Control: no-cache, must-revalidate"
echo "Expires: Sat, 26 Jul 1997 05:00:00 GMT"
echo

POWER_FILE=/var/power

if  [ ! -f $LIGHT_CTRL ]; then
	echo "Cannot access /var/power, possibly this is not a SP2"
	exit 0
fi

cat $POWER_FILE

