/*
 * @author Marius Pozniakovas
 * QueenProblem.java
 * N Queen Problem
 */

import java.util.Set;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Iterator;
import java.util.BitSet;

public class QueenProblem implements Runnable {
	
	private Set<String> solutions;
	private int start, end, n;

	QueenProblem(int n, Set<String> solutions, int start, int end) {
		this.solutions = solutions;
		this.start = start;
		this.end = end;
		this.n = n;
	}
	
	public static void main(String args[]) {
		
		Set<String> solutions = Collections.synchronizedSet(new HashSet<>());
        ArrayList<Thread> threads = new ArrayList<>();
        
		//board size and queen count
		int boardSize = 10; //Integer.parseInt(args[0]);
		//threads
		int threadCount = 5; //Integer.parseInt(args[1]);
		//count of boards shown
		int displayLimit = 1; //Integer.parseInt(args[1]);
		
		if (Runtime.getRuntime().availableProcessors() < threadCount) {
			System.err.print("Number of threads (" + threadCount + ") "
					+ "exceeds available threads on this CPU (" + 
					Runtime.getRuntime().availableProcessors() + ")");
			System.exit(1);
		}
        
        //get time
        long startTime = System.nanoTime();
        for (int i = 0; i < boardSize; i += boardSize / threadCount) {
        	Thread t = new Thread(new QueenProblem(boardSize, solutions, i, Math.min(i + boardSize / threadCount, boardSize)));
        	t.start();
        	threads.add(t);
        }
        
        //wait for threads to finish
	    try {
	        for (int i = 0; i < threads.size(); i++) {
	            threads.get(i).join();
	        }
	    } catch (InterruptedException e) {
	        System.out.println("Thread interrupted.");
	    }
	    
	    long endTime = System.nanoTime();
        long duration = (endTime - startTime) / 1000000;
        System.out.println("found " + solutions.size() + " solutions in " + duration + " milliseconds\n");
        
        Iterator<String> i = solutions.iterator();
        int k = 0;
        while (i.hasNext() && k < displayLimit) {
        	String solution = (String) i.next();
        	for (int r = 0; r < boardSize; r++) {
        		for (int c = 0; c < boardSize; c++) {
        			if (r == solution.charAt(c)) {
        				System.out.print("Q ");
        			} else {
            			System.out.print(". ");	
        			}
        		}
        		System.out.println("");
        	}
        	System.out.println("");
        	k++;
        	
        }
	    
	}
	
	public void run() {
		// True = Queen
		BitSet rows = new BitSet(n);
		
		//Iterate through rows between start and end in the first column placing a queen in each
		for (int r = start; r < end; r++) {
            StringBuilder s = new StringBuilder((char)r + "");
            rows.flip(r);
            bruteForce(1, s, solutions, rows);
            rows.flip(r);
        }
	}
	
	public void bruteForce(int c, StringBuilder solution, Set<String> solutions, BitSet rows) {
		if (c == n) {
			solutions.add(solution.toString());
			return;
		}
		
		//go through every row and if a queen can be placed, recurse for next columns 
		for (int r = 0; r < n; r++) {
			if (canPutQueen(r, c, solution, rows)) {
				rows.flip(r);
				//cast r to a char and append it to the solution string
				solution.append((char)r);
				bruteForce(c + 1, solution, solutions, rows);
				rows.flip(r);
				solution.setLength(solution.length() - 1);
			}
		}
	}
	
	public boolean canPutQueen(int r, int c, StringBuilder solution, BitSet rows) {
		int queen;
		// A queen can attack at most 3 squares on a previous column
		// So only check 3 squares
		if (rows.get(r)) return false;
		for (int i = 1; i <= c; i++) {
			queen = solution.charAt(c - i);
			if (queen == (r - i) || queen == (r + i)) return false;
		}
		return true;
	}
}
