public class SensoresRobot {
    public static void main(String[] args) {
        int[] sensores = {120, 85, 210, 150};
        int umbral = 100;

        for (int i = 0; i < sensores.length; i++) {
            System.out.println("Sensor " + (i + 1) + ": " + sensores[i] + " cm");
            if (sensores[i] < umbral) {
                System.out.println(" Advertencia: Obstáculo demasiado cerca");
            }
        }
    }
}
