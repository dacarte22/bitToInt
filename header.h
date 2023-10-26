int exponentiate(int num, int exp) {
    for (int i = 0; i < exp; i++)
        num = num * num;
    return num;
}
