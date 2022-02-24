# This tells first occurrence in my $PATH the bash command can be found.
#! /usr/bin/bash

# A Calendar date variable is created
date=$(date)

echo --------------------------------------------------------

# The date is outlined
echo Doing traceroute at $date >> MTN-to-Airtel.txt

# A paris-traceroute is made to Airtel public IPv4 Address
paris-traceroute 8.8.8.8 >> MTN-to-Airtel.txt

# The date is outlined
echo Ended traceroute at $date >> MTN-to-Airtel.txt