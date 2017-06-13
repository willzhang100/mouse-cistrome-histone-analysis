#!/bin/awk -f 

BEGIN {
    FS = "\t"
    sum = 0
}
{
    FDR = $1
    sum += FDR
}
END {
    print sum / NR
}
