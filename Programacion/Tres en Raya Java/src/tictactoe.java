import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class tictactoe {
    public static void main(String[] args) {
        System.out.println("Bienvenido al juego Tic Tac Toe." +
                "\n" + "Las reglas de este juego son muy sencillas. El tablero de juego será este:" +
                "\n\t\t" + "|_||_||_|" +
                "\n\t\t" + "|_||_||_|" +
                "\n\t\t" + "|_||_||_|" +
                "\n" + "Y deberá ganar a su oponente." +
                "\n" + "Antes deberá elegir ficha, X ó O." + "\n");

        game();
    }

    public static String chooseChip() {
        System.out.println("¿Qué ficha quiere elegir?");
        Scanner playerChoice = new Scanner(System.in);
        return playerChoice.nextLine();
    }

    public static void game() {
        chooseChip();
        String serverChip = server.serverChip;
        String clientChip = client.clientChip;

        int turn = (Math.random() <= 0.5) ? 1 : 2;


        while (true) {
            if (turn == 1) {
                System.out.println("Es turno del Server, ¿En qué celda quieres posicionar tu ficha?");
            } else {
                System.out.println("Es turno del Cliente, ¿En qué celda quieres posicionar tu ficha?");
            }
        }
    }
}