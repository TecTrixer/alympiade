import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.URL;
 
class HelloWorld{
    /**
     * Stores the target HTML page at the specified location
     * 
     * @param URL the URL, which should be addressed
     * @param path the path, which is needed, to store the file
     */
    public void saveTo(URL targetURL, String path) {
        String content = getContent(targetURL);
         
            writeStringToFile(path, content);
    }
     
    private void writeStringToFile(String filename, String s){
        PrintWriter out = null;
        try {
            out = new PrintWriter(filename);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        out.print(s);
        out.close();
    }
     
    static private String getContent(URL targetURL) {
        String line = "";
        String lines = "";
         
        try {
            BufferedReader in = new BufferedReader(new InputStreamReader(targetURL.openStream()));
 
            while ((line = in.readLine()) != null){
                System.out.println(line);
 
                lines = lines + line;
            }
            in.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
 
        return lines;
    }
     
    public static void main(String[] args) {
        URL website = new URL("https://www.google.de/");
        System.out.print(website);
     }
}