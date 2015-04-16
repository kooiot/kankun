#!/bin/sh

echo "Content-Type: text/plain"
echo "Cache-Control: no-cache, must-revalidate"
echo "Expires: Sat, 26 Jul 1997 05:00:00 GMT"
echo

LIGHT_CTRL=/sys/class/leds/i-konke:yellow:light/brightness

if  [ ! -f $LIGHT_CTRL ]; then
	echo "There is no leds control, possibly this is not a SP2"
	exit 0
fi

case "$QUERY_STRING" in
  state) 
    case "`cat $LIGHT_CTRL`" in
      0) echo "OFF";;
      1) echo "ON" ;;
    esac;;
  on) 
    echo 1 > $LIGHT_CTRL
    echo OK;;
  off) 
    echo 0 > $LIGHT_CTRL
    echo OK;;
  toggle)
    case "`cat $LIGHT_CTRL`" in
      0) echo 1 > $LIGHT_CTRL
         echo "ON";;
      1) echo 0 > $LIGHT_CTRL
         echo "OFF" ;;
    esac;;    
esac

