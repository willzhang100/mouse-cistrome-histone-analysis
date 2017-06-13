#!/bin/awk -f 

BEGIN {
    FS = "\t"
    OFS = ";"
    previous = ""
    stdev = "None"
    n = 0
    sum = 0
    sum_squares = 0
    cistrone = ""  
}
{
    filename = "histone_mouse/" $8
    histone = $7

    if (histone != previous && previous != "") {
        if (n > 1)
            stdev = sqrt((1/n)*(sum_squares - ((sum)^2)/n))
        print cistrone,previous,stdev
        n = 0
        sum = 0
        sum_squares = 0
        previous = histone
        cistrone = $1
    }

    cmd = "wc -l " filename " | awk '{ print $1 }'"
    cmd | getline n_incr
    close(cmd)

    n += n_incr

    cmd = "cat " filename " | awk -f fdr.awk | awk -f sum.awk"
    cmd | getline sum_incr
    close(cmd)

    sum += sum_incr


    cmd = "cat " filename " | awk -f fdr_squared.awk | awk -f sum.awk"
    cmd | getline sum_squares_incr
    close(cmd)

    sum_squares += sum_squares_incr

    if (previous == "") {
        previous = histone
        cistrone = $1
    }
}
END {
    print cistrone,previous,stdev
}
