import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    System.out.println();
    Scanner scan = new Scanner(System.in);
    System.out.println("Enter a country");
    String fc = scan.nextLine();
    System.out.println("Enter an adverb");
    String adv1 = scan.nextLine();
    System.out.println("Enter an adjective");
    String adj1 = scan.nextLine();
    System.out.println("Enter an animal");
    String aml = scan.nextLine();
    System.out.println("Enter a verb ending in -ing");
    String ving1 = scan.nextLine();
    System.out.println("Enter a verb");
    String verb1 = scan.nextLine();
    System.out.println("Enter a verb ending in -ing");
    String ving2 = scan.nextLine();
    System.out.println("Enter an adverb");
    String adv2 = scan.nextLine();
    System.out.println("Enter an adjective");
    String adj2 = scan.nextLine();
    System.out.println("Enter a place");
    String place = scan.nextLine();
    System.out.println("Enter a liquid");
    String liquid = scan.nextLine();
    System.out.println("Enter a body part");
    String bodyPart = scan.nextLine();
    System.out.println("Enter a verb");
    String verb2 = scan.nextLine();
    scan.close();

    System.out.println();
    System.out.println("You want to travel to " + fc + " for a nice, quiet vacation.");
    System.out.println("While exploring the scenery and the many tourist spots that are somehow very empty, you find yourself lost.  Ahead lies a river.  You step closer to it, and lights appear on the other side.  Rescuers?");
    System.out.println("But wait..the river..are those..bull sharks?!?  You have to get across the river " + adv1 + ".");
    System.out.println("Those " + adj1 + " bull sharks love preying on " + aml + ". You wouldn't want to be their next target!");
    System.out.println("You remember hearing that the river animals love to go " + ving1 + ".  Is this the river that the locals were talking about?  Their words ring in your mind, reminding you of all their warnings. ");
    System.out.println("Make sure you are " + ving2 + " when you see these river animals.");
    System.out.println("Keep in mind that these river animals like to hang in " + place);
    System.out.println("Be wary of the " + liquid + " landing on your " + bodyPart + " or you will " + verb2);
    System.out.println("Somehow, you " + adv2 + " make it across the river.  You " + verb1 + " to the " + adj2 + " rescuers, who scold you for running off and getting yourself in danger near those dolphins.  Wait? Dolphins?");
    System.out.println("You look back at the river, which had become as calm as the breeze. No creatures in sight. ");
    System.out.println("THE END");
  }
}