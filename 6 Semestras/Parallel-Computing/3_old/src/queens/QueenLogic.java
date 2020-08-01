/*
 * @author Marius
 * version 1.0
 * QueenLogic.java
 */

package queens;

import java.util.concurrent.atomic.AtomicInteger;

public class QueenLogic extends Thread {
	private int n;
	private int places[];
	private int column;
	private static AtomicInteger count = new AtomicInteger(0);

	public QueenLogic(int n, int column, int places[]) {
		this.n = n;
		this.column = column;
		this.places = places;
	}
		
	public boolean isSafe(int row, int column) {
		int tempColumn = column - 1;
		for (; tempColumn >= 1; tempColumn--) {
			if ((places[tempColumn] - row) == 0) {
				return false;
			}
			
			int rowDiff = places[column] - places[tempColumn];
			
			if ((rowDiff == column - tempColumn) || 
					(rowDiff == tempColumn - column)) {
				return false;
			}
		}
		return true;
	}
	
	public void place() {
		for(int i = 1; i <= n; i++) {
			places[column] = i;
			if (isSafe(i, column)) {
				if (column < n) {
					column++;
					place();
					column--;
				}
				
				if (column == n) {
					count.incrementAndGet();
					System.out.println("Count: " + count);
					//System.out.println("Thread ID: " + Thread.currentThread().getId());
				}
			}
		}
	}
	
	@Override
	public void run() {
		place();
	}
	
	public static int getCount() {
		return count.get();
	}
	
}
	
