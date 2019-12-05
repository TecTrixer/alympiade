import com.gargoylesoftware.htmlunit.WebClient;
import com.gargoylesoftware.htmlunit.html.HtmlElement;
import com.gargoylesoftware.htmlunit.html.HtmlOption;
import com.gargoylesoftware.htmlunit.html.HtmlPage;
import com.gargoylesoftware.htmlunit.html.HtmlSelect;


public class WebTest {
  public static void main(String[] args) throws Exception {

    final WebClient webClient = new WebClient();
    final HtmlPage page = webClient.getPage("website name here");
    System.out.print(page);
    webClient.closeAllWindows();
  }
}
