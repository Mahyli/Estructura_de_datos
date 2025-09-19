public class Inventario {
    public static void main(String[] args) {
        int[][] inventario = {
            {101, 50, 20},
            {102, 30, 15},
            {103, 80, 10}
        };

        System.out.println("Inventario:");
        for (int i = 0; i < inventario.length; i++) {
            for (int j = 0; j < inventario[i].length; j++) {
                System.out.print(inventario[i][j] + " ");
            }
            System.out.println();
        }

        // Producto específico (segundo, índice 1)
        int cantidad = inventario[1][1];
        int precio = inventario[1][2];
        int valorTotal = cantidad * precio;

        System.out.println("\nValor total del producto con ID " + inventario[1][0] + ": " + valorTotal);

        // Actualizar stock después de vender 10
        inventario[1][1] -= 10;
        System.out.println("Nuevo stock del producto " + inventario[1][0] + ": " + inventario[1][1]);
    }
}
