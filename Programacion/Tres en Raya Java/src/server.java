import java.net.ServerSocket;
import java.net.Socket;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.ClassNotFoundException;
import java.util.Scanner;

/**
 * Esta clase implementa el servidor para la conexión del programa
 */
public class server {

    public static String serverChip = null;

    public static void main(String[] args) throws IOException, ClassNotFoundException {
        // Variable estática SOCKET del server
        ServerSocket server;
        // Variable estática PUERTO de la conexión
        int port = 12345;
        // Crear objeto server mediante la clase ServerSocket pasandole el puerto
        server = new ServerSocket(port);

        while(true) {
            // Informar de que se está esperando la conexión
            System.out.println("[ESPERANDO] Esperando conexión del cliente...");
            // Aceptar la conexión en el socket
            Socket socket = server.accept();
            // Informar de que el cliente se ha conectado correctamente
            System.out.println("[ÉXITO] El cliente se ha conectado con éxito");

            /*tictactoe.main(args);
            serverChip = tictactoe.chooseChip();*/

            // Crear objeto de entrada válido
            ObjectInputStream ois = new ObjectInputStream(socket.getInputStream());
            // Obtener el mensaje del cliente
            String message = (String) ois.readObject();
            // Mostrar el mensaje recibido
            System.out.println("[MENSAJE] El mensaje recibido es: " + message);
            // Crear objeto de salida válido
            ObjectOutputStream oos = new ObjectOutputStream(socket.getOutputStream());

            Scanner userInput = new Scanner(System.in);
            String userMessage = userInput.nextLine();

            oos.writeObject("" + userMessage);

            // Cerrar el server definitivamente si el mensaje del cliente es "exit"
            if(message.equalsIgnoreCase("exit")) break;
        }
        // Informar del cierre de la conexión
        System.out.println("[SALIENDO] Cerrando la conexión...");
        // Cerrar la conexión
        server.close();
    }
}
