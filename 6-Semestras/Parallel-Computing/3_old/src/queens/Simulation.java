/*
 * @author Marius
 * version 1.0
 * Simulation.java
 */

package queens;


public class Simulation {

	public static void main(String[] args) {
		
		//number of queens
		//int n = 20; //make 
		int n = Integer.parseInt(args[0]); //later
		
		//number of threads
		int threadCount = Integer.parseInt(args[1]);
		
		if (Runtime.getRuntime().availableProcessors() < threadCount) {
			System.err.print("Number of threads (" + threadCount + ") exceeds available threads on this CPU (" + Runtime.getRuntime().availableProcessors() + ")");
			System.exit(1);
		}
		
		long startingTime = System.currentTimeMillis();


		
		System.out.println("Working time: " + +(float)(System.currentTimeMillis()-startingTime)/1000+" s."); 
		System.out.println("Possible placements: " + QueenLogic.getCount());
	}

}
