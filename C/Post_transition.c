#include <stdio.h>
#include <stdlib.h>
#define MAX_STRING_LENGTH 6

struct package
{
	char* id;
	int weight;
};

typedef struct package package;

struct post_office
{
	int min_weight;
	int max_weight;
	package* packages;
	int packages_count;
};

typedef struct post_office post_office;

struct town
{
	char* name;
	post_office* offices;
	int offices_count;
};

typedef struct town town;



void print_all_packages(town t) {
    int i = 0;
    printf("%s:\n", t.name);
    while (i < t.offices_count){
        printf("\t%d:\n", i);
        int j = 0;
        while (j < t.offices[i].packages_count){
            printf("\t\t%s\n", t.offices[i].packages[j].id);
            j++;
        }
        i++;
    }
}

void send_all_acceptable_packages(town* source, int source_office_index, town* target, int target_office_index) {
    int i = 0;
    int *pack;
    int sent = 0;
    pack = malloc(sizeof(int) * source->offices[source_office_index].packages_count);
    while (i < source->offices[source_office_index].packages_count)
    {
        if (source->offices[source_office_index].packages[i].weight <= target->offices[target_office_index].max_weight && source->offices[source_office_index].packages[i].weight >= target->offices[target_office_index].min_weight){
            pack[sent] = i;
            sent++;
        }
        i++;
    }
    package *copy_source;
    package *copy_target;
    copy_source = source->offices[source_office_index].packages;//malloc(source->offices[source_office_index].packages_count);
    copy_target = target->offices[target_office_index].packages;//malloc(target->offices[target_office_index].packages_count);
    source->offices[source_office_index].packages = malloc((source->offices[source_office_index].packages_count - sent)*sizeof(package));
    target->offices[target_office_index].packages = malloc((target->offices[target_office_index].packages_count + sent)*sizeof(package));
    i = 0;
    int s_i = 0;
    int t_i = 0;
    while (t_i < target->offices[target_office_index].packages_count)
    {
        target->offices[target_office_index].packages[t_i] = copy_target[t_i];
        t_i++;
    }
    while (i < source->offices[source_office_index].packages_count){
        int k = 0;
        while (k < sent && pack[k] != i)
            k++;
        if (k == sent)
        {
            source->offices[source_office_index].packages[s_i] = copy_source[i];
            s_i++;
        }
        else{
            target->offices[target_office_index].packages[t_i] = copy_source[i];
            t_i++;
        }
        i++;
    }
    source->offices[source_office_index].packages_count -= sent;
    target->offices[target_office_index].packages_count += sent;
}

town town_with_most_packages(town* towns, int towns_count) {
    int max = 0;
    int i = 0;
    int found = 0;
    while (i < towns_count){
        int pack = 0;
        int j = 0;
        while (j< towns[i].offices_count){
            pack += towns[i].offices[j].packages_count;
            j++;
        }
        if (pack > max)
        {max = pack;
        found = i;}
        i++;
    }
    return (towns[found]);
}

int str_equals(char *s, char *t)
{
    int i = 0;
    while (s[i] != '\0' && t[i] != '\0' && s[i] == t[i])
        i++;
    if (s[i] != '\0' || t[i] != '\0')
        return (0);
    return (1);
}

town* find_town(town* towns, int towns_count, char* name) {
    int found = 0;
    int i = 0;
    while (i < towns_count && found == 0) {
        if (str_equals(towns[i].name, name) == 1)
            found = 1;
        i++;
    }
    return (&towns[i-1]);
}

int main()
{
	int towns_count;
	scanf("%d", &towns_count);
	town* towns = malloc(sizeof(town)*towns_count);
	for (int i = 0; i < towns_count; i++) {
		towns[i].name = malloc(sizeof(char) * MAX_STRING_LENGTH);
		scanf("%s", towns[i].name);
		scanf("%d", &towns[i].offices_count);
		towns[i].offices = malloc(sizeof(post_office)*towns[i].offices_count);
		for (int j = 0; j < towns[i].offices_count; j++) {
			scanf("%d%d%d", &towns[i].offices[j].packages_count, &towns[i].offices[j].min_weight, &towns[i].offices[j].max_weight);
			towns[i].offices[j].packages = malloc(sizeof(package)*towns[i].offices[j].packages_count);
			for (int k = 0; k < towns[i].offices[j].packages_count; k++) {
				towns[i].offices[j].packages[k].id = malloc(sizeof(char) * MAX_STRING_LENGTH);
				scanf("%s", towns[i].offices[j].packages[k].id);
				scanf("%d", &towns[i].offices[j].packages[k].weight);
			}
		}
	}
	int queries;
	scanf("%d", &queries);
	char town_name[MAX_STRING_LENGTH];
	while (queries--) {
		int type;
		scanf("%d", &type);
		switch (type) {
		case 1:
			scanf("%s", town_name);
			town* t = find_town(towns, towns_count, town_name);
			print_all_packages(*t);
			break;
		case 2:
			scanf("%s", town_name);
			town* source = find_town(towns, towns_count, town_name);
			int source_index;
			scanf("%d", &source_index);
			scanf("%s", town_name);
			town* target = find_town(towns, towns_count, town_name);
			int target_index;
			scanf("%d", &target_index);
			send_all_acceptable_packages(source, source_index, target, target_index);
			break;
		case 3:
			printf("Town with the most number of packages is %s\n", town_with_most_packages(towns, towns_count).name);
			break;
		}
	}
	return 0;
}
