#include <stdio.h>
#include "filter.h"

int main() {
    struct Item goods[] = {
        {"Ковер", 2000, "green"},
        {"Диван для отдыха", 0, "black"}
    };

    printf("По одному полю:\n");
    filterByField(goods, 2, 1, "title");

    printf("По нескольким полям:\n");
    filterByField(goods, 2, 2, "title", "price");

    return 0;
}
