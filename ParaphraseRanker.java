import org.goobs.sim.*;

public class PhraseRanker {
    public static void main(String[] args) {
        DistSim distsim = DistSim.load("sim/etc/distsim.ser.gz");

        InputStream in;
        BufferedReader reader;

        in = new FileInputStream(new File(args[0]));
        reader = new BufferedReader(new InputStreamReader(in));

        String line;
        while ((line = reader.readLine()) != null) {
            line = line.trim();
            if (line.isEmpty()) {
                phrase = reader.readLine();
                if (phrase != null) {
                    phrase = phrase.trim();
                }
            } else {
                DistSim.Similarity sim = distsim.sim(phrase, line).get();
                System.out.println("Phrase: " + phrase);
                System.out.println("PP: " + line);
                System.out.println("Sim: " + sim.cos());
            }
        }
        
        reader.close();
    }
}
