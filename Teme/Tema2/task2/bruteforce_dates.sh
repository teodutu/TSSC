#! /bin/bash
# Copyright: https://stackoverflow.com/a/28226339

start=2001-1-1
end=2101-1-1

startdate=$(date -I -d "$start")
enddate=$(date -I -d "$end")

d="$startdate"
while [ "$d" != "$enddate" ]; do
	curl -c cookies -f --silent --output backup.tar.gz http://localhost:8080/backup-$d.tar.gz && echo $d && exit 0
	d=$(date -I -d "$d + 1 day")
done

# caut 1f 8b 08. nu exista ca nu-s pe aceeasi linie in xxd => caut : 8b08 si gasesc
# cu 1f inainte la 00381dd0 => addr = 00381dcf
