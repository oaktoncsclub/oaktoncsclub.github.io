import java.util.Scanner;

public class BlockChain {

	private int pos;
	public static double time;
	public static double trans;
	static int count = 0;
	public static BlockChain[] items = new BlockChain[10];

	public BlockChain(double time, double trans) {

		this.time = time;
		this.trans = trans;
	}
	
	private static double getTime()
	{
		return time;
	}
	
	private static double getTrans()
	{
		return trans;
	}
	
	public static BlockChain[] stash(BlockChain arg) {
		if (count < items.length - 1) {
			arg.pos = count - 1;
			count++;
			items[count] = arg;
			return items;
		} else {
			resize();
			stash(arg);
			return items;
		}
	}

	private static void resize() {
		BlockChain[] storage = new BlockChain[items.length * 2];
		for (int i = 0; i < items.length; i++) {
			storage[i] = items[i];
		}
		items = storage;
	}
	
	public String toString()
	{
		String checker = new String();
		for(int i = 0; i < count ; i++)
		{
			checker += items[i].getTime() + " " + items[i].getTrans();
		}
		return checker;
	}
	public static void main(String args[])
	{
		Scanner items = new Scanner(System.in);
		System.out.println("How many blocks?");
		int j = items.nextInt();
		for(int i = 0; i <j; i++)
		{
		System.out.print("Enter time: ");
		double x = items.nextDouble();
		//items.close();
		System.out.println("");
		//Scanner sc = new Scanner(System.in);
		System.out.print("Enter transaction");
		double trans = items.nextDouble();
		
		BlockChain arg = new BlockChain(x,trans);
		stash(arg);
		System.out.println("" + arg.toString());
		}
		items.close();
	}
}
