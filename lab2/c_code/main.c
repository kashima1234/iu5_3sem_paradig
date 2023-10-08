#include "set_lib.h"
#include "set_operation.h"
#include "set_input.h"





int main()
{
    const int max_length = 10; 
    char s1[max_length], s2[max_length];

   if (!get_user_input(s1, s2, max_length))
		{
		   return EXIT_FAILURE;
		}

    printf("Levenshtein distance between %s and %s is %d\n", s1, s2, set_levenshtein_dist(s1, s2));

    return EXIT_SUCCESS;
}
