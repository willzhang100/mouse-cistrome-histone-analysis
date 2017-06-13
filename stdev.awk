#!/bin/awk -f 

BEGIN {
    FS = "\t"
    sum = 0
    sum_squares = 0
}
{
    sum += $1
    sum_squares += $1 ^ 2
}
END {
    print sqrt((1/NR) * ((sum_squares) - (((sum)^2)/NR)))  
}
