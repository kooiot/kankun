#!/bin/sh

echo "Content-Type: text/plain"
echo "Cache-Control: no-cache, must-revalidate"
echo "Expires: Sat, 26 Jul 1997 05:00:00 GMT"
echo

ONLINE=/etc/ver/online
OFFLINE=/etc/ver/offline

if  [ ! -f $ONLINE ]; then
	ONLINE=/etc/online.txt
	OFFLINE=/etc/offline.txt
fi

case "$QUERY_STRING" in
  online) 
	  cat $ONLINE;;
  offline) 
	  cat $OFFLINE;;
esac

