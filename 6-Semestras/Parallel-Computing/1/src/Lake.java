/*
 * Lake.java
 * Class for creating a lake for fishers to fish in
 * @author Marius Pozniakovas
 * https://klevas.mif.vu.lt/~rvck/lygska/pratybos/uzduot1.html
 * Lygiagretus skaiciavimai #1
 */

import java.util.HashMap;
import java.util.Map;
import java.util.Random;


public class Lake {
	private String name;
	private Map<String, Integer> fishesInLake;
	
	
	public Lake(String name) {
		this.name = name;
		
		this.fishesInLake = new HashMap<String, Integer>() {{
			put("Cod", 100);
			put("Bass", 100);
			put("Plaice", 100);
			put("Turbot", 100);
			put("Pollack", 100);
			put("Black bream", 100);
			put("Mackerel", 100);
			put("Ray", 100);
			put("Shark", 100);
			put("Garfish", 100);
		}};
	}
	
	public int getFishCount(String fishName) {
		return fishesInLake.get(fishName);
	}
	
	public String getRandomFishName() {
		Object randomName = fishesInLake.keySet().toArray()
				[new Random().nextInt(fishesInLake.keySet().toArray().length)];
		return randomName.toString();

	}
	
	public void removeFish(String fishName) {
		this.fishesInLake.replace(fishName, fishesInLake.get(fishName) - 1);
	}
	
	public void displayFishes() {
		System.out.println("Fishes in " + this.name + ":");
		System.out.println(fishesInLake);
	}
	
}
