#include <stdio.h>

int AND(int a, int b) {
    return a && b;
}

int OR(int a, int b) {
    return a || b;
}

int NOT(int a) {
    return !a;
}

int NOR(int a, int b) {
    return !(a || b);
}

int NAND(int a, int b) {
    return !(a && b);
}

int XOR(int a, int b) {
    return a != b;
}

int XNOR(int a, int b) {
    return a == b;
}

int main() {
    int a = 1, b = 1;

    printf("AND: %d\n", AND(a, b));
    printf("OR: %d\n", OR(a, b));
    printf("NOT(a): %d\n", NOT(a));
    printf("NOR: %d\n", NOR(a, b));
    printf("NAND: %d\n", NAND(a, b));
    printf("XOR: %d\n", XOR(a, b));
    printf("XNOR: %d\n", XNOR(a, b));

    return 0;
}
