/*
 * Main.java
 * Main class for starting the script
 * @author Marius Pozniakovas
 * https://klevas.mif.vu.lt/~rvck/lygska/pratybos/uzduot1.html
 * Lygiagretus skaiciavimai #1
 */

public class Main {
	public static void main(String[] args) {
		
		//lake
		Lake lake = new Lake ("Salantai");
		
		//fish started
		lake.displayFishes();
		
		//start fishing
		Team.startFishing(lake);
		
		//fish left
		lake.displayFishes();
		
		
				
	}
}
