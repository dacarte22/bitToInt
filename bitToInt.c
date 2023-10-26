#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
//#include <string.h>
#include "header.h"





int main(int argc, char *argv[]) {
    char byte[9];//Array of characters representing one byte, each character representing one bit as "0" or "1"
    //For automated testing
    /*for (int i = 0; i < argc; i++) {
        printf("argv[%d]: %s\n", i, argv[i]);
    }
    for (int i = 0; i < argc; i++) {
        byte[i] = *argv[i];
        printf("byte[%d]: %d\n", i, byte[i]);
        printf("argv[%d]: %s\n", i, argv[i]);
    }*/

    
    //strcpy(byte, argv[1]);
    for (int i = 0; i < 8 ; i++) {
        byte[i] = argv[1][i];
        //printf("byte[%c]: %c\n", i, byte[i]);
    }
    //For user interaction
    /*
    printf("Enter 8 numbers in binary: ");
    if (fgets(byte, sizeof(byte), stdin)) {
        printf("You entered: %s\n", byte);
    } else {
        printf("Input error.\n");
        return 1;
    }
    */

    int length = sizeof(byte) / sizeof(byte[0]);
    // Reverse the array
    for (int i = 0; i < length / 2; i++) {
        int temp = byte[i];
        byte[i] = byte[length - 1 - i];
        byte[length - 1 - i] = temp;
    }

    int res = 0;
    for (int i = 1; byte[i] !='\0'; i++) {
        if (byte[i] == '1') 
            res += exponentiate(2, i-1);
        else
            continue;
    }
    //printf("The integer value of the byte array is %d \n", res);
    printf("%d\n", res);
    return 0;
}

