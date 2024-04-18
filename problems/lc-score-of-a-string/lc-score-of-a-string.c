#include <stdlib.h>

int scoreOfString(char* s) {
    int len=strlen(s);
    int score=0;
    for (int i = 0; i< len-1; i++){
        score+=abs((int)s[i]-(int)s[i+1]);
    }
    return score;
}