#!/bin/bash

function printHelpMenu {
	echo -e "=== Flags === \n\
--processid=<PROCESS_ID>    The process id of the container \n\
--port=<PORT>		    The port to record \n\
--host=<HOST>		    The host to record traffic to/from"
}

while [ $# -gt 0 ]; do
	case "$1" in
		--processid=*) PROCESS_ID="${1#*=}" ;;
		--port=*) PORT="${1#*=}" ;;
		--host=*) HOST="${1#*=}" ;;
		--help | -h) printHelpMenu
		             exit ;;
		*) echo "Invalid Argument"
		   exit 1 ;;
	esac
	shift
done

if [[ ${HOST} == '' || ${PORT} == '' ]]
then
	echo "--port and --host flags are required"
	exit 1 
fi

TCPDUMP_COMMAND="/usr/sbin/tcpdump -vvvni any host ${HOST}"
if [[ ! -z "$PORT" ]]
then
	TCPDUMP_COMMAND+=" and port ${PORT}"
fi

nsenter -n -t $PROCESS_ID $TCPDUMP_COMMAND
