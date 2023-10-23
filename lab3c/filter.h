#ifndef FILTER_H
#define FILTER_H

struct Item {
    char *title;
    int price;
    char *color;
};

void filterByField(struct Item items[], int itemCount, ...);

#endif
