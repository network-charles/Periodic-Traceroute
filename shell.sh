# This tells first occurrence in my $PATH the bash command can be found.
#! /usr/bin/bash

date=$(date)


echo ---------------------------------------------- >> Whatsapp.txt


echo Doing Paris traceroute at $date >> Whatsapp.txt


paris-traceroute www.whatsapp.com >> Whatsapp.txt


echo Ended Paris traceroute at $date >> Whatsapp.txt


echo ---------------------------------------------- >> Whatsapp.txt
