import java.util.Random;

/*
 * @author Marius Pozniakovas
 * Lygiagreciu antra uzduotis (0 variantas)
 * 
 */
public class TestThread extends Thread {
	
	private Barrier barrier;
	String threadNumber;
	
	public TestThread(Barrier barrier, String threadNumber) {
		this.barrier = barrier;
		this.threadNumber = threadNumber;
	}

	public static void main(String[] args) {
		
		int expectedConnections = 4;
		
		Barrier barrier = new Barrier(expectedConnections);
		
		TestThread thread1 = new TestThread(barrier, "1");
		TestThread thread2 = new TestThread(barrier, "2");
		TestThread thread3 = new TestThread(barrier, "3");
		TestThread thread4 = new TestThread(barrier, "4");
		
		thread1.start(); 
		thread2.start(); 
		thread3.start(); 
		thread4.start();
		
		
		try {
			thread1.join(); 
			thread2.join(); 
			thread3.join();
			thread4.join();
			
		} catch (InterruptedException exc) {
			exc.printStackTrace();
		}
	}
		
	@Override
	public void run() {
		
		Random rand = new Random();
		final int LEVELS = 5;
		int triesToPassLevel = 0;
		
		try {
			for (int i = 1; i <= LEVELS; i++) {
				
				while (true) {
					
					triesToPassLevel++;

					if (rand.nextInt(1000) > 750) {
						System.out.println("Level " + i + " passed."
								+ " Thread name: " + this.threadNumber + ". Number of tries: "
								+ triesToPassLevel);
						
						triesToPassLevel = 0;
						barrier.waitBarrier();
						
						break;
					}
					
				}
			
			}

		} catch (InterruptedException exc) {
			exc.printStackTrace();
		}
		
		System.out.println("Thread " + this.threadNumber + " closed.");
	}
		
		
	

}
