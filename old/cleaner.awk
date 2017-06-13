#!/bin/awk -f 

BEGIN {
    FS = ","
    OFS = ";"
}
{
    if(NF > 7) {
        FUSED = $2 "," $3
        $2 = FUSED 
        $3 = $4
        $4 = $5
        $5 = $6
        $6 = $7
    } 
    print $1,$2,$3,$4,$5,$6,$7 >> "output-cleaned.txt"     
}
END {
    print "Finished cleaning the output file."
}
