/*
 * @author Marius
 * Lygiagreciu antra uzduotis (0 variantas)
 * Barrier.java klase kuri 
 * 
 *	0*. Barjeras - su duomen� apsikeitimu
 *	Objektas inicializuojamas "s�veikoje" dalyvaujan�i� gij� skaiciumi (N).
 *	Pagrindin� operacija -
 *	    int  waitBarier(int reik�m�).
 *	Kiekviena �� metod� i�kvietusi gij� laukia, kol kviet�j� skai�ius taps lygus N.
 *	Tada visos N gijos "paleid�iamos" - metodas gra�ina asociatyvios operacijos (pvz. sumos)
 *	su visomis "reik�m�mis" rezultat� - o barjeras reinicializuojamas, t.y., paruo�iamas
 *	sekan�iam waitBarier() kvietiniui.
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
