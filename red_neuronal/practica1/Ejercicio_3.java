import java.util.Scanner;

public class Cine {
    public static void main(String[] args) {
        int[][] cine = new int[4][5];
        Scanner sc = new Scanner(System.in);

        System.out.println("Mapa de asientos (0=libre, 1=ocupado):");
        for (int i = 0; i < cine.length; i++) {
            for (int j = 0; j < cine[i].length; j++) {
                System.out.print(cine[i][j] + " ");
            }
            System.out.println();
        }

        System.out.print("\nElige la fila (0-3): ");
        int fila = sc.nextInt();
        System.out.print("Elige el asiento (0-4): ");
        int col = sc.nextInt();

        // Marcar asiento como ocupado
        cine[fila][col] = 1;

        System.out.println("\nMapa actualizado:");
        for (int i = 0; i < cine.length; i++) {
            for (int j = 0; j < cine[i].length; j++) {
                System.out.print(cine[i][j] + " ");
            }
            System.out.println();
        }

        // Contar libres
        int libres = 0;
        for (int i = 0; i < cine.length; i++) {
            for (int j = 0; j < cine[i].length; j++) {
                if (cine[i][j] == 0) libres++;
            }
        }
        System.out.println("\nTotal de asientos libres: " + libres);
    }
}
