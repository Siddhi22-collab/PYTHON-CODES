from xmlrpc.client import UNSUPPORTED_ENCODING
from numpy import std


UNSUPPORTED_ENCODING namespace std

// Function to check if the Sudoku matrix is valid
int isValid(vector<vector<int>> mat){
  
    // Track of numbers in rows, columns, and sub-matrix
    vector<vector<int>> rows(10, vector<int>(10, 0));
    vector<vector<int>> cols(10, vector<int>(10, 0));
    vector<vector<int>> subMat(10, vector<int>(10, 0));

    for (int i = 0; i < 9; i++){
        for (int j = 0; j < 9; j++){

            // Skip empty cells
            if (mat[i][j] == 0)
                continue;

            // Current value
            int val = mat[i][j]; 

            // Check for duplicates in row
            if (rows[i][val] == 1)
                return false;

            // Mark as seen
            rows[i][val] = 1; 

            // Check for duplicates in column
            if (cols[j][val] == 1)
                return false;

            // Mark as seen
            cols[j][val] = 1; 

            // Check for duplicates in sub-grid
            int idx = (i / 3) * 3 + j / 3;
            if (subMat[idx][val] == 1)
                return false;

            // Mark as seen
            subMat[idx][val] = 1; 
        }
    }

    return true;
}

int main(){
    vector<vector<int>> mat = 
                     {{7, 9, 2, 1, 5, 4, 3, 8, 6}, 
                     {6, 4, 3, 8, 2, 7, 1, 5, 9},
                     {8, 5, 1, 3, 9, 6, 7, 2, 4},
                     {2, 6, 5, 9, 7, 3, 8, 4, 1},
                     {4, 8, 9, 5, 6, 1, 2, 7, 3},
                     {3, 1, 7, 4, 8, 2, 9, 6, 5},
                     {1, 3, 6, 7, 4, 8, 5, 9, 2},
                     {9, 7, 4, 2, 1, 5, 6, 3, 8},
                     {5, 2, 8, 6, 3, 9, 4, 1, 7}};

    cout << (isValid(mat) ? "true" : "false") << "\n";

    return 0;
}
