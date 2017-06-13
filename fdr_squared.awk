#!/bin/awk -f
BEGIN {
    FS = "\t"
}
{
    print $9^2
}
END {

}
