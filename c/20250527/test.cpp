#include <stdlib.h>
#include <stdio.h>

unsigned LowBit(unsigned x)
{
    return x & (-x);
}

unsigned Letter(unsigned x)
{
    unsigned x1 = (x & 0x22222222) >> 1;
    unsigned x2 = (x & 0x44444444) >> 2;
    unsigned x3 = (x & 0x88888888) >> 3;

    x = x3 & (x1 | x2);
    x = x & (x >> 16);
    x = x & (x >> 8);
    x = x & (x >> 4);
    return x;
}

int main()
{
    unsigned n = 7;
    // printf("S[%u]\n", n);
    // printf("+ T[%u]\n", n);
    // n = n - LowBit(n);
    // printf("+ T[%u]\n", n);
    // n = n - LowBit(n);
    // printf("+ T[%u]\n", n);
    // n = n - LowBit(n);
    // printf("+ T[%u]\n", n);

    printf("0x%x, is letter 0x%x\n", 0xabcdefab, Letter(0xabcdefab));
    printf("0x%x, is letter 0x%x\n", 0xa0a0a0a0, Letter(0xa0a0a0a0));
    printf("0x%x, is letter 0x%x\n", 0x11111111, Letter(0x11111111));

    return 0;
}
