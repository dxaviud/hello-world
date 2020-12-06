#include <iostream>
#include <conio.h>
#include <windows.h>
using namespace std;

bool gameOver;
const int width = 20;
const int height = 20;
int x, y, fruitX, fruitY, score;
int tailX[100], tailY[100];
int tailLength;
enum eDirection {STOP = 0, LEFT, RIGHT, UP, DOWN};
eDirection dir;
void setup()
{
    gameOver = false;
    dir = STOP;
    x = width/2;
    y = height/2;
    fruitX = rand() % width;
    fruitY = rand() % height;
    score = 0;

}
bool isTail(int x, int y);
void draw()
{
    system("cls");
    cout << "Score: " << score << endl;
    for (int i = 0; i < width; i++)
        cout << "#";
    cout << endl;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (j==0 || j==width-1)
                cout << "#";
            else if (i == y && j == x)
                cout << "O";
            else if (i == fruitY && j == fruitX)
                cout << "F";
            else if (isTail(j, i))
                cout << "o";
            else
                cout << " ";
        }
        cout << endl;
    }

    for (int i = 0; i < width; i++)
        cout << "#";
    cout << endl;
}

bool isTail(int x, int y)
{
    for (int k = 0; k < tailLength; k++)
        {
            if (tailX[k] == x && tailY[k] == y)
                return true;
        }
    return false;

}
void input()
{
    if (_kbhit())
    {
         switch(_getch())
         {
         case 'a':
            if (dir != RIGHT)
                dir = LEFT;
            break;
         case 'd':
            if (dir != LEFT)
                dir = RIGHT;
            break;
         case 's':
            if (dir != UP)
                dir = DOWN;
            break;
         case 'w':
            if (dir != DOWN)
                dir = UP;
            break;
         case 'x':
            gameOver = true;
            break;
         }
    }

}
void logic()
{
    int prevX = tailX[0];
    int prevY = tailY[0];
    int prev2X, prev2Y;

    tailX[0] = x;
    tailY[0] = y;

    for (int i = 1; i < tailLength; i++)
    {
        prev2X = tailX[i];
        prev2Y = tailY[i];
        tailX[i] = prevX;
        tailY[i] = prevY;
        prevX = prev2X;
        prevY = prev2Y;
    }
    switch(dir)
    {
    case LEFT:
        x--;
        break;
    case RIGHT:
        x++;
        break;
    case UP:
        y--;
        break;
    case DOWN:
        y++;
        break;
    }
    if (x == 0 || x == width-1 || y == -1 || y == height)
        gameOver = true;
    for (int k = 0; k < tailLength; k++) {
        if (tailX[k] == x && tailY[k] == y)
        {
            gameOver = true;
            break;
        }

    }
    if (x == fruitX && y == fruitY)
    {
        tailLength++;
        score += 10;
        fruitX = rand() % width;
        fruitY = rand() % height;
    }


}
int main()
{

    setup();
    while (!gameOver)
    {
        draw();
        input();
        logic();
        Sleep(100);
    }
    cout << "game over.";

    return 0;
}
