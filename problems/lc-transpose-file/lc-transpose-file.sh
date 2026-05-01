# Read from the file file.txt and print its transposed content to stdout.
awk '{
        for (i = 1; i <= NF; i++) {
            s[NR, i] = $i
        }
    }
    NF > max_nf { max_nf = NF }
    END {
    for (i = 1; i <= max_nf; i++) {
        for (j = 1; j <= NR; j++) {
            printf "%s%s", s[j, i], (j == NR ? "" : " ")
        }
    print ""
    }
}' file.txt