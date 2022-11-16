//https://www.hackerrank.com/challenges/structuring-the-document/problem
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5

struct word {
    char* data;
};

struct sentence {
    struct word* data;
    int word_count;//denotes number of words in a sentence
};

struct paragraph {
    struct sentence* data  ;
    int sentence_count;//denotes number of sentences in a paragraph
};

struct document {
    struct paragraph* data;
    int paragraph_count;//denotes number of paragraphs in a document
};

int is_alpha(unsigned int a)
{
    return ((a >= 'a' && a <= 'z') || (a >= 'A' && a <= 'Z'));
}

int get_paragraphs(char *text){
    int i = 0;
    int count = 0;
    while (text[i] != '\0')
    {
        if (text[i] == '\n')
            count++;
        i++;
    }
    count++;
    return (count);
}

int get_sentences(char *text, int *i){
    int count = 0;
    while (text[*i] != '\n' && text[*i] != '\0')
    {
        if (text[*i] == '.')
            count++;
        (*i)++;
    }
    return (count);
}

int get_words(char *text, int *i){
    int count = 0;
    while (text[*i] != '.')
    {
        if (text[*i] == ' ')
            count++;
        (*i)++;
    }
    count++;
    return (count);
}

struct document create_doc(char* text){
    struct document doc;
    doc.paragraph_count = get_paragraphs(text);
    doc.data = malloc(doc.paragraph_count * sizeof(struct paragraph));
    int parag = 0;
    int i = 0;
    while (parag < doc.paragraph_count)
    {
        doc.data[parag].sentence_count = get_sentences(text, &i);
        doc.data[parag].data = malloc(doc.data[parag].sentence_count * sizeof(struct sentence));
        if (!is_alpha(text[i]) && text[i] != '\0')
            i++;
        parag++;
    }
    parag = 0;
    i = 0;
    while (parag < doc.paragraph_count)
    {
        int sent = 0;
        while (sent < doc.data[parag].sentence_count)
        {
            doc.data[parag].data[sent].word_count = get_words(text, &i);
            doc.data[parag].data[sent].data = malloc(doc.data[parag].data[sent].word_count * sizeof(struct word));
            sent++;
            i++;
            if (text[i] == ' ')
                i++;
        }
        parag++;
    }
    return (doc);
}


struct document get_document(char* text) {
    struct document doc = create_doc(text);
    int parag = 0;
    int sent;
    int wor;
    int letter;
    int pos = 0;
    while (parag < doc.paragraph_count)
    {
        sent = 0;
        while (sent < doc.data[parag].sentence_count)
        {
            wor = 0;
            while (wor < doc.data[parag].data[sent].word_count)
            {
                letter = 0;
                while (is_alpha(text[pos + letter]))
                {
                    letter++;
                }
                doc.data[parag].data[sent].data[wor].data = malloc((letter + 1) * sizeof(char));
                memmove(doc.data[parag].data[sent].data[wor].data, text + pos, letter);
                doc.data[parag].data[sent].data[wor].data[letter] = '\0';
                pos += letter;
                while (!is_alpha(text[pos]) && text[pos] != '\0')
                    pos++;
                wor++;
            }
            sent++;
        }
        parag++;
    }
    return (doc);
}


struct word kth_word_in_mth_sentence_of_nth_paragraph(struct document Doc, int k, int m, int n) {
    return (Doc.data[n-1].data[m-1].data[k-1]);
}

struct sentence kth_sentence_in_mth_paragraph(struct document Doc, int k, int m) { 
    return (Doc.data[m-1].data[k-1]);
}

struct paragraph kth_paragraph(struct document Doc, int k) {
    return (Doc.data[k-1]);
}


void print_word(struct word w) {
    printf("%s", w.data);
}

void print_sentence(struct sentence sen) {
    for(int i = 0; i < sen.word_count; i++) {
        print_word(sen.data[i]);
        if (i != sen.word_count - 1) {
            printf(" ");
        }
    }
}

void print_paragraph(struct paragraph para) {
    for(int i = 0; i < para.sentence_count; i++){
        print_sentence(para.data[i]);
        printf(".");
    }
}

void print_document(struct document doc) {
    for(int i = 0; i < doc.paragraph_count; i++) {
        print_paragraph(doc.data[i]);
        if (i != doc.paragraph_count - 1)
            printf("\n");
    }
}

char* get_input_text() {	
    int paragraph_count;
    scanf("%d", &paragraph_count);

    char p[MAX_PARAGRAPHS][MAX_CHARACTERS], doc[MAX_CHARACTERS];
    memset(doc, 0, sizeof(doc));
    getchar();
    for (int i = 0; i < paragraph_count; i++) {
        scanf("%[^\n]%*c", p[i]);
        strcat(doc, p[i]);
        if (i != paragraph_count - 1)
            strcat(doc, "\n");
    }

    char* returnDoc = (char*)malloc((strlen (doc)+1) * (sizeof(char)));
    strcpy(returnDoc, doc);
    return returnDoc;
}

int main() 
{
    char* text = get_input_text();
    struct document Doc = get_document(text);

    int q;
    scanf("%d", &q);

    while (q--) {
        int type;
        scanf("%d", &type);

        if (type == 3){
            int k, m, n;
            scanf("%d %d %d", &k, &m, &n);
            struct word w = kth_word_in_mth_sentence_of_nth_paragraph(Doc, k, m, n);
            print_word(w);
        }

        else if (type == 2) {
            int k, m;
            scanf("%d %d", &k, &m);
            struct sentence sen= kth_sentence_in_mth_paragraph(Doc, k, m);
            print_sentence(sen);
        }

        else{
            int k;
            scanf("%d", &k);
            struct paragraph para = kth_paragraph(Doc, k);
            print_paragraph(para);
        }
        printf("\n");
    }     
}