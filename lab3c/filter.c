#include <stdio.h>
#include <stdarg.h>
#include <string.h>
#include "filter.h"

void print_info(const char *key, const char *value)
{
    printf("%s: %s", key, value);
}

void filterByField(struct Item items[], int itemCount, ...)
{
    va_list args;
    va_start(args, itemCount);
    int numFields = va_arg(args, int);
    char buf[256] = {'\0'};

    for (int i = 0; i < numFields; ++i)
    {
        printf("{");
        const char *field = va_arg(args, const char *);
        int flag = 0, found = 0;
        for (int j = 0; j < itemCount; ++j)
        {
            buf[0] = '\0';
            if (flag)
            {
                printf(", ");
            }
            flag = 1;
            if (strcmp(field, "title") == 0)
            {
                if (items[j].title != NULL)
                {
                    sprintf(buf, "%s", items[j].title);
                }
                found = 1;
            }
            else if (strcmp(field, "price") == 0)
            {
                if (items[j].price > 0)
                {
                    sprintf(buf, "%d", items[j].price);
                    found = 1;
                }
            }
            else if (strcmp(field, "color") == 0)
            {
                if (items[j].color != NULL)
                {
                    sprintf(buf, "%s", items[j].color);
                }
                found = 1;
            }
            if (found)
                print_info(field, buf);
        }
        printf("}\n");
    }

    va_end(args);
}
