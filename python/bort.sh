#!/usr/bin/env bash

# used to rename our modules from addresses like 101, 102, 103, ... to 1, 2, 3, ...

counter=1
while [ $counter -le 30 ]
do
	echo "renaming $(($counter+100)) to $(($counter))"
	
	./set_addr.py -o $(($counter+100)) -n $(($counter))
	((counter++))
	
	read -p "Press enter to continue"
done
