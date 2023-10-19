#include "set_operation.h"

int set_min(int a, int b, int c)
{
	if (a <= b && a <= c)
		return a;
	if (b <= a && b <= c)
		return b;
	return c;

}

//Variables m and n store the lengths of the input strings s1 and s2 respectively. 
//An array d of size (m + 1) x (n + 1) is created to store intermediate distances during the computation.


int set_levenshtein_dist(const char *s1, const char *s2)
{
	int m = strlen(s1);
	int n = strlen(s2);
        int d[m + 1][n +1];

    for (int i = 0; i <= m; i++) 
        d[i][0] = i;
    for (int j = 0; j <= n; j++) 
        d[0][j] = j;
//d loop
    for (int j = 1; j <= n; j++) 
    {
        for (int i = 1; i <= m; i++) 
        {
            if (s1[i - 1] == s2[j - 1]) 
            {
                d[i][j] = d[i - 1][j - 1];
            } else 
            {
                d[i][j] = set_min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + 1);
            }
        }
    }

    return d[m][n];
}


