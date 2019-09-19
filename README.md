# Truth-Table
A script to write out the truth tables to two logical statements.

^ : and

|| : or

\- : negation

=> : conditional

Statement A:

        [(P ^ -Q) => (Q || R)] ^ S

Statement B:

        (R || S) ^ (P => Q)




Output:

        p q r s   A B

        0 0 0 0   0 0

        0 0 0 1   1 1

        0 0 1 0   0 1

        0 0 1 1   1 1

        0 1 0 0   0 0

        0 1 0 1   1 1

        0 1 1 0   0 1

        0 1 1 1   1 1

        1 0 0 0   0 0

        1 0 0 1   0 0

        1 0 1 0   0 0

        1 0 1 1   1 0

        1 1 0 0   0 0

        1 1 0 1   1 1

        1 1 1 0   0 1

        1 1 1 1   1 1
