# Matrix Calculator Gauss Method

This application is designed to solve matrix equations by the Gaussian method in steps and without fractions. Most online calculators solve with fractions, which can be a red rag for your teacher. This calculator solves by steps and you can visually check or solve the problem using the application.

    Gauss(
        Matrix(
            [
                MatrixString([a11, a12, a13], x1),
                MatrixString([a21, a22, a23], x2),
                MatrixString([a31, a32, a33], x3),
                MatrixString([ani, ..., ann], xn),
            ]
        )
    ).count()
