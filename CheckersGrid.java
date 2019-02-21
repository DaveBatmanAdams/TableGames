import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;
import java.io.*;

public class CheckersGrid
{
	public static void main( String args[])
	{
		JFrame window;
		Container content;
		ButtonListener listener = new ButtonListener();


		window = new JFrame("Classic Checkers");
		content = window.getContentPane();
		content.setLayout(new GridLayout(1, 1));

		JPanel boardPanel = new JPanel();
		boardPanel.setLayout(new GridLayout(10, 10));

		//THESE ARE EXPERIMENTAL PIECES BE CAREFUL
		int currentX;
		int currentY = 0;

		for(int j = 0; j < 5; j++)
		{	
			currentX = 0;

			for (int i=0 ; i<10 ; i++ )
			{
				BoardSpace btn = new BoardSpace();


				if(i % 2 == 0)
					{
						btn.setForeground(Color.WHITE);
						btn.setBackground(Color.WHITE);
						btn.setOpaque(true);
					}
				else
					{
						btn.setForeground(Color.BLACK);
						btn.setBackground(Color.BLACK);
						btn.setOpaque(true);
						btn.setBorderPainted(false);
					}

				btn.setX(currentX);
				btn.setY(currentY);

				currentX++;

				btn.setFont(new Font("Arial", Font.PLAIN, 40));
				btn.setText(".");

				//DEBUGGING TOOL TO BE REMOVED/CHANGED LATER...PLACES TEST PIECE AT BOTTOM OF BOARD
				/*if(btn.getX() == 4 && btn.getY() == 9)
					{
						btn.setForeground(Color.PINK);
					}
				*/
				boardPanel.add( btn );
				btn.addActionListener( listener ); 
			}

			currentX = 0; 
			currentY++;

			for (int i=0 ; i<10 ; i++ )
			{

				BoardSpace btn = new BoardSpace();

				if(i % 2 == 0)
					{
						btn.setForeground(Color.BLACK);
						btn.setBackground(Color.BLACK);
						btn.setOpaque(true);
						btn.setBorderPainted(false);
					}
				else
					{
						btn.setForeground(Color.WHITE);
						btn.setBackground(Color.WHITE);
						btn.setOpaque(true);
						btn.setBorderPainted(false);
					}
				
				btn.setX(currentX);
				btn.setY(currentY);

				currentX++;
				
				btn.setFont(new Font("Arial", Font.PLAIN, 40));
				btn.setText(".");

				//DEBUGGING TOOL TO BE REMOVED/CHANGED LATER...PLACES TEST PIECE AT BOTTOM OF BOARD
				/*if(btn.getX() == 4 && btn.getY() == 9)
					{
						btn.setForeground(Color.PINK);
					}
				*/
				boardPanel.add( btn );
				btn.addActionListener( listener ); 
			}
			currentY++;
		}

		content.add(boardPanel);
		window.setSize( 640,480 );
		window.setVisible( true );

	} //End Main
} //End checkers class


//This class tells our button what to do if it gets clicked
class ButtonListener implements ActionListener
{
	public void actionPerformed(ActionEvent e )
	{
		BoardSpace clickedSpace = (BoardSpace) e.getSource();

		//THIS IS A DEBUGGING TOOL USED TO TRACK CLICKED COORDINATES IN TERMINAL. REMOVE WITH FINAL VERSION
		System.out.println(clickedSpace.getX() + " " + clickedSpace.getY());

		//IMPLEMENT MOVEMENT INTERFACE BELOW

		//IF A PIECE IS NOT SELECTED, WAIT FOR PIECE TO BE SELECTED...IF EMPTY SPACE IS CLICKED DO NOTHING

		//IF A PIECE IS SELECTED ALREADY, WAIT FOR VALID CLICK TO MOVE PIECE...INVALID CLICKS RESULT IN DESELECTING PIECE

		//MAY HAVE TO ALLOW USER TO MAKE MANY ERRANT CLICKS...MAY NEED WHILE LOOP??

		//START BY MAKING A SINGLE PIECE MOVE...THEN ADD TWO PIECES THAT JUMP...THEN ADD A THIRD PIECE, 
		//WHICH IS JUMPED BY ENEMY COLOR AND SPARED BY ALLY COLOR

	}
		
}


//This class makes sure our Buttons know their coordinates, and if there is a piece on them
class BoardSpace extends JButton
{
	boolean hasPiece = false;
	boolean selectedPiece = false;

	int xCoordinate;

	int yCoordinate;

	public void setX(int newX)
	{
		xCoordinate = newX;
	}

	public void setY(int newY)
	{
		yCoordinate = newY;
	}

	public int getX()
	{
		return xCoordinate;
	}

	public int getY()
	{
		return yCoordinate;
	}


	//Use this if a space has a piece moving onto or off of it
	public void flipHasPiece()
	{
		if(hasPiece == true)
			{
				hasPiece = false;
				//SET TO BOARD COLOR
				////ADD COLOR CHANGES LATER WHEN YOU FIGURE OUT HOW TO REVERT TO ORIGINAL COLOR
				
				//this.setForeground(Color.BLACK);
			}
		else
			{
				hasPiece = true;
				//SET TO PIECE COLOR
				//ADD COLOR CHANGES LATER WHEN YOU FIGURE OUT HOW TO REVERT TO ORIGINAL COLOR
				
				//this.setForeground(Color.PINK);
			}

	}

	//If the space has a piece, make it let up green
	public void selectSpace()
	{
		

		if(this.hasPiece == true)
			{
				//ADD COLOR CHANGES LATER WHEN YOU FIGURE OUT HOW TO REVERT TO ORIGINAL COLOR
				
				//this.setForeground(Color.GREEN);

				selectedPiece = true;

			}

	}

	//Once you've made a move, change the color back to normal
	//Don't know how to revert color back to normal yet. Make it blue for now
	public void deselectSpace()
	{
		selectedPiece = false;

		////ADD COLOR CHANGES LATER WHEN YOU FIGURE OUT HOW TO REVERT TO ORIGINAL COLOR
		
		//this.setForeground(Color.BLUE);
	}



}




