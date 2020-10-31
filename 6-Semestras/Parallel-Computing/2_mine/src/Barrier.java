/*
 * @author Marius
 * Lygiagreciu antra uzduotis (0 variantas)
 * Barrier.java klase kuri 
 * 
 *	0*. Barjeras - su duomenø apsikeitimu
 *	Objektas inicializuojamas "sàveikoje" dalyvaujanèiø gijø skaiciumi (N).
 *	Pagrindinë operacija -
 *	    int  waitBarier(int reikðmë).
 *	Kiekviena ðá metodà iðkvietusi gijà laukia, kol kvietëjø skaièius taps lygus N.
 *	Tada visos N gijos "paleidþiamos" - metodas graþina asociatyvios operacijos (pvz. sumos)
 *	su visomis "reikðmëmis" rezultatà - o barjeras reinicializuojamas, t.y., paruoðiamas
 *	sekanèiam waitBarier() kvietiniui.
 *
 */
public class Barrier {
	
	private int value;
	private int tempValue = 0;
	
	private int connections = 0;
	private int expectedConnections;
	
	
	public Barrier(int expectedConnections) {
		this.expectedConnections = expectedConnections;
		this.value = 0;
		
	}
	
	public synchronized void waitBarrier() throws InterruptedException {
		
		//wait Barrier workflow
		
		//1. caller connects and we add his value
		connections++;
		
		//2. now wait for everyone to connect
		if (connections != expectedConnections) {
			wait();
		}
		//3. IF everyone is connected
		else {
			
			//tell everyone
			notifyAll();
			
			//reset the connections
			connections = 0;
		
		}
		
		return;
		
	}
	
}
