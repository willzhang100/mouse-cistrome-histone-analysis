#!/bin/awk -f 

BEGIN {
    FS = "\t"
    OFS = ";"
}
{
    histone = $7
    filename = "histone_mouse/" $8 
    
    print filename
	   
    cmd = "cat " filename " | awk -f width.awk | awk -f mean.awk" 
    cmd | getline mean 
    close(cmd)
    
    cmd = "cat " filename " | awk -f width.awk | awk -f stdev.awk" 
    cmd | getline stdev
    close(cmd) 

    cmd = "wc -l " filename " < " filename
    cmd | getline n
    close(cmd)
    
    print histone, mean, stdev, n
    print histone, mean, stdev, n >> "summary-width.txt" 
}
END {
    print "Finished executing summarize.awk."
}
