import java.util.Scanner;

public class SwitchCaseKullanimi {
    public static void main(String[] args) {
        Scanner scan =new Scanner(System.in);
        System.out.print("Lutfen bir sayi giriniz: ");
        int sayi = scan.nextInt();
        switch (sayi) {
            case 3:
                System.out.println("Sayi 1 e esittir");
                
                break;
        
            default:
                System.out.println("GEcesriz bir sayi girimistir");
                break;
        }
    }
}
