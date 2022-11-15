//https://www.hackerrank.com/challenges/small-triangles-large-triangles/problem

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

float area(triangle tr)
{
    float p= (tr.a + tr.b + tr.c)/2;
    return (p*(p-tr.a)*(p-tr.b)*(p-tr.c));
}

void sort_by_area(triangle* tr, int n) {
	/**
	* Sort an array a of the length n
	*/
    triangle v;
    for (int i=0; i < n-1; i++)
    {
        for (int j = 0; j < n-i-1; j++)
        {
            if (area(tr[j]) > area(tr[j+1]))
            {
                v = tr[j];
                tr[j] = tr[j+1];
                tr[j+1] = v;
            }
        }
    }
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}
