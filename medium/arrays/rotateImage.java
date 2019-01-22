class Solution {
    public void rotate(int[][] matrix) { 
        int N = matrix.length;
        // For every layer, rotate
        // For an NxN matrix, there are N/2 layers
        for (int i = 0; i < N/2; i++) {
            // Rotate layer:
            // For each layer, every number has to be rotated 90 degrees.
            // To do this, move along the left-most column of the layer.
            // For every element in this column - to the 2nd last element -
            // rotate them using a temp array of four elements. The first
            // element in the temp array is the current element in left-most
            // column that gets rotated 90 degrees onto where the 2nd element
            // of the temp array is in the matrix, which also rotates 90 degrees
            // onto where the 3rd element of the temp array is in the matrix,
            // and so on onto the last element which gets rotated 90 degrees to
            // where the first element in the temp array was in the matrix before
            // rotating.
            for (int row = 0; row < ((N-1) - 2*i); row++) {
                // Fill temp
                int[] temp = new int[4];
                temp[0] = matrix[row+i][i];
                temp[1] = matrix[i][(N-1)-(row+i)];
                temp[2] = matrix[(N-1)-(row+i)][(N-1)-i];
                temp[3] = matrix[(N-1)-i][row+i];
                
                // Modify matrix
                matrix[row+i][i] = temp[3];
                matrix[i][(N-1)-(row+i)] = temp[0];
                matrix[(N-1)-(row+i)][(N-1)-i] = temp[1];
                matrix[(N-1)-i][row+i] = temp[2];
            }
        }
    }
}