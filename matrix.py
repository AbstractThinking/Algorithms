class Matrix(object):

    def __init__(self, mtx):
        self.set_matrix(mtx);

    @staticmethod
    def create(rows, cols, vals=0):
        return [[vals for j in range(cols)] for i in range(rows)];

    def get_matrix(self):
        return self._mtx;

    def set_matrix(self, mtx):
        self._is_mtx(mtx);
        self._mtx = mtx;

    @staticmethod
    def add(A, B):
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))];

    @staticmethod
    def opposite(A):
        return [[-A[i][j] for j in range(len(A[0]))] for i in range(len(A))];

    @staticmethod
    def subtract(A, B):
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))];

    @staticmethod
    def multiply(A, B):
        Matrix.Matrix.strassen_multiply_recursive(A, B);

    @staticmethod
    def multiply_iterative(A, B):
        r = len(A);
        n = len(A[0]);
        m = len(B);
        c = len(B[0]);
        
        C = self.create(r,c);
        
        for i in range(r):
            for j in range(c):
                for k in range(n):
                    C[i][j] += A[i][k] * B[k][j];
                    
        return C;


    @staticmethod
    def square_matrix_multiply_recursive(A, B):
        if len(A) == 1:
            return [[A[0][0] * B[0][0]]];
        
        A_slices = Matrix._split_matrix(A);
        B_slices = Matrix._split_matrix(B);
        
        C = Matrix.create(2,2);
        
        C[0][0] = Matrix.add(square_matrix_multiply_recursive(A_slices[0][0], B_slices[0][0]),
                    square_matrix_multiply_recursive(A_slices[0][1], B_slices[1][0]));
        C[0][1] = Matrix.add(square_matrix_multiply_recursive(A_slices[0][0], B_slices[0][1]),
                    square_matrix_multiply_recursive(A_slices[0][1], B_slices[1][1]));
        C[1][0] = Matrix.add(square_matrix_multiply_recursive(A_slices[1][0], B_slices[0][0]),
                    square_matrix_multiply_recursive(A_slices[1][1], B_slices[1][0]));
        C[1][1] = Matrix.add(square_matrix_multiply_recursive(A_slices[1][0], B_slices[0][1]),
                    square_matrix_multiply_recursive(A_slices[1][1], B_slices[1][1]));
    
        return C;

    @staticmethod
    def strassen_multiply_recursive(A, B):
        
        if len(A) == 1:
            return [[A[0][0] * B[0][0]]];
        
        A_slices = Matrix._split_matrix(A);
        B_slices = Matrix._split_matrix(B);
        
        S = [None for i in range(10)]
        
        S[0] = Matrix.subtract(B_slices[0][1], B_slices[1][1]);
        S[1] = Matrix.add(A_slices[0][0], A_slices[0][1]);
        S[2] = Matrix.add(A_slices[1][0], A_slices[1][1]);
        S[3] = Matrix.subtract(B_slices[1][0], B_slices[0][0]);
        S[4] = Matrix.add(A_slices[0][0], A_slices[1][1]);
        S[5] = Matrix.add(B_slices[0][0], B_slices[1][1]);
        S[6] = Matrix.subtract(A_slices[0][1], A_slices[1][1]);
        S[7] = Matrix.add(B_slices[1][0], B_slices[1][1]);
        S[8] = Matrix.subtract(A_slices[0][0], A_slices[1][0]);
        S[9] = Matrix.add(B_slices[0][0], B_slices[0][1]);

        P = [None for i in range(7)]

        P[0] = Matrix.strassen_multiply_recursive(A_slices[0][0],S[0]);
        P[1] = Matrix.strassen_multiply_recursive(S[1],B_slices[1][1]);
        P[2] = Matrix.strassen_multiply_recursive(S[2],B_slices[0][0]);
        P[3] = Matrix.strassen_multiply_recursive(A_slices[1][1],S[3]);
        P[4] = Matrix.strassen_multiply_recursive(S[4],S[5]);
        P[5] = Matrix.strassen_multiply_recursive(S[6],S[7]);
        P[6] = Matrix.strassen_multiply_recursive(S[8],S[9]);

        C = Matrix.create(2,2);
        
        C[0][0] = Matrix.add(Matrix.subtract(Matrix.add(P[4], P[3]), P[1]), P[5]);
        C[0][1] = Matrix.add(P[0], P[1]);
        C[1][0] = Matrix.add(P[2], P[3]);
        C[1][1] = Matrix.subtract(Matrix.subtract(Matrix.add(P[4], P[0]), P[2]), P[6]);

        return [r1 + r2 for r1, r2 in zip(C[0][0] + C[1][0], C[0][1] + C[1][1])];

    def _is_mtx(self, mtx):
        check_errs = {
            'empty': lambda mtx: len(mtx) == 0 or len(mtx[0]) == 0,
            'list': lambda obj: not isinstance(obj, list),
            'numeric': lambda obj: isinstance(obj, (int, float)),
            'length': lambda line, size: len(line) != length,
        };

        if check_errs['list'](mtx):
            raise TypeError;

        if check_errs['empty'](mtx):
            raise ValueError;

        for i, line in enumerate(mtx):
            if i == 0:
                length = len(line);
            
            if check_errs['length'](line, length):
                raise ValueError;
            
            if check_errs['list'](line):
                raise TypeError;

                
    @staticmethod
    def _split_matrix(A):
        f_r = len(A);
        h_r = f_r // 2 
        f_c = len(A[0]);
        h_c = f_c // 2
        
        slices = [[Matrix._slice_matrix(A, 0, h_r, 0, h_c),
                Matrix._slice_matrix(A, 0, h_r, h_c, f_c)],
                [Matrix._slice_matrix(A, h_r, f_r, 0, h_c),
                Matrix._slice_matrix(A, h_r, f_r, h_c, f_c)]];
        
        return slices;


    @staticmethod
    def _slice_matrix(A, min_row, max_row, min_col, max_col):
        B = [];
            
        for row in A[min_row:max_row]:
            B.append(row[min_col:max_col]);
            
        return B;
