import java.io.BufferedReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class FileReader {
    public static void wyswietlZawartoscPliku(String nazwaPliku) {
        try {
            Path sciezka = Paths.get(nazwaPliku);
            BufferedReader reader = Files.newBufferedReader(sciezka, StandardCharsets.UTF_8);
            
            System.out.println("Zawartość pliku " + nazwaPliku + ":");
            String linia;
            while ((linia = reader.readLine()) != null) {
                System.out.println(linia);
            }
            reader.close();
            
        } catch (IOException e) {
            System.out.println("Błąd: Nie można odczytać pliku " + nazwaPliku);
            System.out.println("Szczegóły błędu: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        String sciezkaPliku = "dane/data.txt"; // domyślna ścieżka do pliku
        wyswietlZawartoscPliku(sciezkaPliku);
    }
} 