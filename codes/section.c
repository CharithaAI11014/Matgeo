#include <stdio.h>
#include <stdlib.h>
#include "libs/geofun.h"
#include "libs/matfun.h"

// Function to calculate the external division point
double **Matsec_ext(double **X, double **Y, int m, double k) {
    double **temp = createMat(2, 1);
    temp[0][0] = (m * Y[0][0] - k * X[0][0]) / (m - k); // x-coordinate
    temp[1][0] = (m * Y[1][0] - k * X[1][0]) / (m - k); // y-coordinate
    return temp;
}

int main() {
    // Define vectors a and b
    double ax = 1.0, ay = 3.0; // Components of vector a
    double bx = 2.0, by = 1.0; // Components of vector b

    // Define points X and Y
    double **X = createMat(2, 1);
    double **Y = createMat(2, 1);

    // Calculate X = 3a + b
    X[0][0] = 3 * ax + bx; // x-component
    X[1][0] = 3 * ay + by; // y-component

    // Calculate Y = a - 3b
    Y[0][0] = ax - 3 * bx; // x-component
    Y[1][0] = ay - 3 * by; // y-component

    // Define ratio for external division
    double m = 2.0, n = 1.0;

    // Calculate point V using the external division formula
    double **V = Matsec_ext(X, Y, m, n);

    // Output the result to console
    printf("Point V: (%.2f, %.2f)\n", V[0][0], V[1][0]);

    // Write results to points.dat
    FILE *file = fopen("points.dat", "w");
    if (file == NULL) {
        perror("Unable to open file");
        return 1;
    }

    // Write points to the file
    fprintf(file, "%.2f, %.2f\n", X[0][0], X[1][0]);
    fprintf(file, "%.2f, %.2f\n", Y[0][0], Y[1][0]);
    fprintf(file, "%.2f, %.2f\n", V[0][0], V[1][0]);

    fclose(file); // Close the file

    // Free allocated memory
    freeMat(X, 2);
    freeMat(Y, 2);
    freeMat(V, 2);

    return 0;
}

