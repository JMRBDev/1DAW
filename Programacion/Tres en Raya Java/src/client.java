import java.net.Socket;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.InetAddress;
import java.lang.ClassNotFoundException;
import java.util.Scanner;

/**
 * Esta clase implementa el cliente para la conexión del programa
 */
public class client {

    public static String clientChip = null;

    public static void main(String[] args) throws IOException, ClassNotFoundException {
        // Variable estática PUERTO de la conexión
        int port = 12345;
        // IP del host servidor (en este caso es LocalHost porque estamos trabajando en la misma máquina)
        InetAddress host = InetAddress.getLocalHost();
        Socket socket = null;
        ObjectOutputStream oos = null;
        ObjectInputStream ois = null;

        while (true) {
            // Crea el socket con el nombre del host y el puerto de conexión
            socket = new Socket(host.getHostName(), port);
            // Crear objeto de salida válido
            oos = new ObjectOutputStream(socket.getOutputStream());
            // Informar de que se está intentando realizar la conexión
            System.out.println("[CONECTANDO] Enviando petición de conexión al servidor...");
            // Informar de que se ha conectado al servidor con éxito
            System.out.println("[ÉXITO] Se ha conectado al servidor con éxito");

            /*tictactoe.main(args);
            clientChip = tictactoe.chooseChip();*/

            Scanner userInput = new Scanner(System.in);
            String userMessage = userInput.nextLine();

            oos.writeObject("" + userMessage);

            // Crear objeto de entrada válido
            ois = new ObjectInputStream(socket.getInputStream());
            // Obtener el mensaje del cliente
            String message = (String) ois.readObject();
            // Mostrar el mensaje recibido
            System.out.println("[MENSAJE] El mensaje recibido es: " + message);

            // Si el cliente decide salir (con exit), cerrar la conexión
            if (userMessage.equalsIgnoreCase("exit")) {
                System.out.println("[SALIENDO] Cerrando la conexión...");
                break;
            }
        }
    }
}