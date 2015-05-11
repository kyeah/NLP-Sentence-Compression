import org.goobs.sim.*;

public class PhraseRanker {
  public static void main(String[] args) {
      System.out.println(args[0]);
      DistSim distsim = DistSim.load("sim/etc/distsim.ser.gz");
      DistSim.Similarity sim = distsim.sim(args[0], args[1]).get();
      System.out.println(sim.cos());
  }
}
