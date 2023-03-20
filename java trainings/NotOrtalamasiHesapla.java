import java.util.Scanner;

public class NotOrtalamasiHesapla {
    public static void main(String[] args) {
        int quiz, vize, finall;
        double ortalama;

        Scanner input = new Scanner(System.in);

    
        System.out.print("Quiz notunuzu giriniz: ");
        quiz = input.nextInt();
        System.out.print("Vize notunuzu giriniz: ");
        vize = input.nextInt();
        System.out.print("Final notounuzu giriniz: ");
        finall = input.nextInt();

        ortalama = (quiz * 0.20) + (vize * 0.35) + (finall * 0.5);

        System.out.println("Ortalamaniz: " + ortalama);
        String sonuc;

        sonuc = (ortalama >= 50) ? "Gectiniz." : "Kaldiniz";

        System.out.print(sonuc);
            
    }
}
