/*
 * Team.java
 * Class for creating fisherman objects
 * @author Marius Pozniakovas
 * https://klevas.mif.vu.lt/~rvck/lygska/pratybos/uzduot1.html
 * Lygiagretus skaiciavimai #1
 */
public class Team {
	
	Fisherman fisherman1;
	Fisherman fisherman2;
	Fisherman fisherman3;	
	Fisherman fisherman4;
	String name;
	int teamscore;
	
	public Team(Fisherman fisherman1, Fisherman fisherman2, Fisherman fisherman3, Fisherman fisherman4, String name) {
		
		this.fisherman1 = fisherman1;
		this.fisherman2 = fisherman2;
		this.fisherman3 = fisherman3;
		this.fisherman4 = fisherman4;
		this.name = name;
		this.teamscore = 0;
	}
	
	
	public static void startFishing(Lake lake) {
		
		
		Fisherman f1 = new Fisherman("Marius", lake);
		Fisherman f2 = new Fisherman("Rokas", lake);
		Fisherman f3 = new Fisherman("Jonas", lake);
		Fisherman f4 = new Fisherman("Mantas", lake);
		//Team team = new Team(f1, f2, f3, f4, "Tironas");
		
		try {
			f1.start();
			f2.start();
			f3.start();
			f4.start();
			
			f1.join();
			f2.join();
			f3.join();
			f4.join();
			
		} catch (InterruptedException exc){
            System.out.println("Something went wrong: " + exc);
        }		
	}	
}
