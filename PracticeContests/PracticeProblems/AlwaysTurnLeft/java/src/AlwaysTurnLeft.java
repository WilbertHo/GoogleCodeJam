import java.io.*;

public class AlwaysTurnLeft {
	public static void main(String[] args) throws Exception {
  try {
    // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedReader br = new BufferedReader(new FileReader(args[0]));
    String line = br.readLine();
    while(line != null) {
      System.out.println(line);
      line = br.readLine();
    }
  } catch(Exception e) {
    System.out.println("exception");
  }
	}
}
