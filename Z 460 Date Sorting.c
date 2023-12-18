#include <stdio.h>
#include <stdlib.h>

// Structure to represent a date
struct Date {
    int day, month, year;
};

// Comparison function for qsort
int compareDates(const void *a, const void *b) {
    const struct Date *dateA = (const struct Date *)a;
    const struct Date *dateB = (const struct Date *)b;

    // Compare years
    if (dateA->year != dateB->year) {
        return dateA->year - dateB->year;
    }

    // Compare months
    if (dateA->month != dateB->month) {
        return dateA->month - dateB->month;
    }

    // Compare days
    return dateA->day - dateB->day;
}

int main() {
    int N;
    scanf("%d", &N);

    // Read dates into an array
    struct Date dates[N];
    for (int i = 0; i < N; i++) {
        scanf("%d %d %d", &dates[i].day, &dates[i].month, &dates[i].year);
    }

    // Sort dates using qsort
    qsort(dates, N, sizeof(struct Date), compareDates);

    // Print sorted dates
    for (int i = 0; i < N; i++) {
        printf("%d %d %d\n", dates[i].day, dates[i].month, dates[i].year);
    }

    return 0;
}


