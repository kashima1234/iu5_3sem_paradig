#include "set_lib.h"


// int get_user_input(char *s1, char *s2, int max_length) 
// {
//     printf("Enter the first word: ");
//     if (scanf("%s", s1) != 1)
//     {
//         printf("Error: Unable to read the first word.\n");
//         return EXIT_FAILURE;
//     }

//     printf("Enter the second word: ");
//     if (scanf("%s", s2) != 1)
//     {
//         printf("Error: Unable to read the second word.\n");
//         return EXIT_FAILURE;
//     }

//     if (strlen(s1) >= max_length || strlen(s2) >= max_length) 
//     {
//         printf("Error: Input words are too long. Maximum allowed length is %d characters.\n", max_length);
//         return EXIT_FAILURE ;
//     }

//     return true;
// }



int has_number(const char *word) {
    for (int i = 0; word[i] != '\0'; i++) {
        if (isdigit(word[i])) {
            return 1; // Return non-zero to indicate presence of a digit
        }
    }
    return 0; // Return 0 to indicate absence of digits
}

int get_user_input(char *s1, char *s2, int max_length) {
    printf("Enter the first word: ");
    scanf("%s", s1);

    printf("Enter the second word: ");
    scanf("%s", s2);

    if (strlen(s1) >= max_length || strlen(s2) >= max_length) {
        printf("Error: Input words are too long. Maximum allowed length is %d characters.\n", max_length);
        return EXIT_SUCCESS;
    }

    if (has_number(s1) || has_number(s2)) {
        printf("Error: Input words contain numbers.\n");
        return EXIT_SUCCESS;
    }

    return EXIT_FAILURE;
}
