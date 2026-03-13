import java.util.Scanner;
public class Filmes {
    public static void main(String[] args) {
        int nota;
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite a nota do filme(de 1 a 5): ");
        nota = entrada.nextInt();
        if(nota == 1){
            System.out.println("Péssimo");
        } else if (nota == 2){
            System.out.println("Ruim");
        } else if (nota == 3){
            System.out.println("Regular");
        } else if (nota == 4){
            System.out.println("Bom");
        } else if (nota == 5){
            System.out.println("Ótimo");
        } else {
            System.out.println("Nota inválida!");
        }
        entrada.close();
    }
}