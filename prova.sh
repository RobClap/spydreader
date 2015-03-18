#!/bin/bash
for x in {1..6}
do
		printf '  \033[00mbi\033[01;31ma\033[00mnco\r'
		usleep 250000
		printf '   \033[00mr\033[01;31mo\033[00msso\r'
		usleep 250000
done

