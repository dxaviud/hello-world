package TicTacToe;

import java.awt.Image;

public abstract class Mark {
    private Image image;

    public Image getImage() {
        return image;
    }

    public void setImage(Image newImage) {
        image = newImage;
    }
    
    public abstract String toString();
}