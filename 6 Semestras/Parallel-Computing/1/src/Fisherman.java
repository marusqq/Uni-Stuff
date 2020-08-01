/*
 * Fisherman.java
 * Class for creating fisherman which will fish in a lake
 * @author Marius Pozniakovas
 * https://klevas.mif.vu.lt/~rvck/lygska/pratybos/uzduot1.html
 * Lygiagretus skaiciavimai #1
 */

import java.util.HashMap;
import java.util.Map;

public class Fisherman extends Thread {
	
	
	private String name;
	Lake lake;
	private Map<String, Integer> fishesCaught;
	
	public Fisherman(String name, Lake lake) {
		this.name = name;
		this.lake = lake;
		
		this.fishesCaught = new HashMap<String, Integer>() {{
			put("Cod", 0);
			put("Bass", 0);
			put("Plaice", 0);
			put("Turbot", 0);
			put("Pollack", 0);
			put("Black bream", 0);
			put("Mackerel", 0);
			put("Ray", 0);
			put("Shark", 0);
			put("Garfish", 0);
		}};
	}
	
	public String getFisherName() {
		return name;
	}
	
	@Override
	public void run() {
		
		final int iterations = 250;
		boolean synch = false;
		
		if (synch)
			System.err.println("Starting synchronized thread [" + this.name + "]");
		else
			System.err.println("Starting not synchronized thread [" + this.name + "]");
			
		//main loop
		for (int i = 0; i < iterations; i++) {	
			fish(synch);
		}
		
		System.err.println("[" + this.name + "] Fishes caught: " + this.fishesCaught);
			
	}
	
	public void fish(boolean synch) {
		
		String fishName;
		
		//if threads are synchronized 
		if (synch) {
																		//kritine kodo vieta - pradzia
			synchronized (lake) {
				//if fish count is 0 or less, we can't catch it
				fishName = lake.getRandomFishName();
				while (lake.getFishCount(fishName) <= 0) {
					fishName = lake.getRandomFishName();
				}
				//remove the fish from the lake
				lake.removeFish(fishName);

																	    //kritine kodo vieta - pabaiga
			}
		}
		
		//if threads aren't synchronized 
		else {
			
			//if fish count is 0 or less, we can't catch it
			fishName = lake.getRandomFishName();
			while (lake.getFishCount(fishName) <= 0) {
				fishName = lake.getRandomFishName();
			}
			//remove the fish from the lake
			lake.removeFish(fishName);

		}
		
		//add the saved fish to fishers basket
		this.fishesCaught.replace(fishName, this.fishesCaught.get(fishName) + 1 ); 

		
		
		
		return;	
	}
}
