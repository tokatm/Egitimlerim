import java.util.Scanner;

import javax.lang.model.util.ElementScanner6;

public class HesapMakinesi {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int sayi1, sayi2, islem;
        System.out.print("Lutfen ilk sayiyiy giriniz: ");
        sayi1 = scan.nextInt();
        System.out.print("Lutfen ikinci sayiyi giriniz: ");
        sayi2 = scan.nextInt();
        System.out.print("Lutfen yapmak istediginiz islemi giriniz: ");
        islem = scan.nextInt();
        if (islem == 1) {
            System.out.println("Toplama? " + (sayi1+sayi2));
        }

        else if (islem == 2) {
            System.out.println("Cikarma: " +(sayi1 - sayi2));
            
        }

        else if (islem == 3){
            System.out.println("Carpma: " +(sayi1*sayi2));
        }

        else if (islem == 4) {
            if (sayi2 == 0) {
                System.out.println("Tanimsiz sonuc.");;
                
            }

            else {
                System.out.println("Bolme: " +(sayi1/sayi2));

            }
        }

        else  {
            System.out.println("Gecersiz bir islem yaptiniz.");

        }
    }
}
