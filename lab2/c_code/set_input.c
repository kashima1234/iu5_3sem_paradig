#include "set_lib.h"


bool get_user_input(char *s1, char *s2, int max_length) 
{
    printf("Enter the first word: ");
    if (scanf("%s", s1) != 1)
    {
        fprintf(stderr, "Error: Unable to read the first word.\n");
        return false;
    }

    printf("Enter the second word: ");
    if (scanf("%s", s2) != 1)
    {
        fprintf(stderr, "Error: Unable to read the second word.\n");
        return false;
    }

    if (strlen(s1) >= max_length || strlen(s2) >= max_length) 
    {
        fprintf(stderr, "Error: Input words are too long. Maximum allowed length is %d characters.\n", max_length);
        return false ;
    }

    return true;
}

