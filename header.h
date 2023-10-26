int exponentiate(int exp) {
    int num = 1;
    for (int i = 0; i < exp; i++)
        num = num * 2;
    return num;
}
