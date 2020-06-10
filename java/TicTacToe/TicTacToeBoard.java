package TicTacToe;

public class TicTacToeBoard {
    
    private Mark[][] boxes;

    public TicTacToeBoard() {
        boxes = new Mark[3][3];
        for (int row = 0; row < boxes.length; row++) {
            for (int col = 0; col < boxes[row].length; col++) {
                boxes[row][col] = new NoMark();
            }
        }
    }

    public Mark getBox(int rowIndex, int colIndex) {
        return boxes[rowIndex][colIndex];
    }
    
}