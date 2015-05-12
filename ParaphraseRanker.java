import org.goobs.sim.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class ParaphraseRanker {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        DistSim distsim = DistSim.load("sim/etc/distsim.ser.gz");

        InputStream in;
        BufferedReader reader;

        in = new FileInputStream(new File(args[0]));
        reader = new BufferedReader(new InputStreamReader(in));

        String line;
        String phrase = null;

        while ((line = reader.readLine()) != null) {
            line = line.trim();
            if (line.isEmpty()) {
                phrase = reader.readLine();
                if (phrase != null) {
                    phrase = phrase.trim();
                }
            } else if (phrase == null) {
                phrase = line;
            } else {
                DistSim.Similarity sim = distsim.sim(phrase, line).get();
                System.out.println("Phrase: " + phrase);
                System.out.println("PP: " + line);
                System.out.println("Sim: " + sim.cos());
                System.out.println("");
            }
        }
        
        reader.close();
    }
}
