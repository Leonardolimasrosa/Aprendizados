import java.util.Scanner;
public class Parça {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite um número inteiro: ");
        int num = entrada.nextInt();
        int divisores = 0;
        for (int i = 1; i <= num; i++){
            if (num % i == 0){
                divisores++;
            }
        }
        if (divisores == 2){
            System.out.println("O número " + num + " é PRIMO!");
        } else {
            System.out.println("O número " + num + " NÃO é PRIMO!");
            System.out.println("Ele possui " + divisores + " divisores");
        }
        entrada.close();
    }
}