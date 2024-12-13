import streamlit as st
import pandas as pd
import plotly.express as px
import os

def wczytaj_pliki_csv(sciezka='dane'):
    pliki_csv = {}
    for plik in os.listdir(sciezka):
        if plik.endswith('.csv'):
            try:
                df = pd.read_csv(os.path.join(sciezka, plik))
                pliki_csv[plik] = df
            except Exception as e:
                st.error(f"Błąd wczytywania pliku {plik}: {e}")
    return pliki_csv

def main():
    st.title('📊 Analiza Danych CSV')
    st.sidebar.header('Opcje')

    # Wczytanie plików CSV
    pliki_csv = wczytaj_pliki_csv()
    
    if not pliki_csv:
        st.warning("Nie znaleziono plików CSV w folderze 'dane'")
        return

    # Wybór pliku
    wybrany_plik = st.sidebar.selectbox(
        'Wybierz plik do analizy:',
        list(pliki_csv.keys())
    )

    # Wyświetlenie danych
    if wybrany_plik:
        df = pliki_csv[wybrany_plik]
        
        st.subheader(f"Podgląd danych z pliku: {wybrany_plik}")
        st.dataframe(df.head())

        st.subheader("Podstawowe informacje")
        col1, col2 = st.columns(2)
        with col1:
            st.write("Liczba wierszy:", df.shape[0])
            st.write("Liczba kolumn:", df.shape[1])
        with col2:
            st.write("Kolumny:", ", ".join(df.columns))

        # Wizualizacja
        st.subheader("Wizualizacja danych")
        
        # Wybór kolumn do wizualizacji
        numeryczne_kolumny = df.select_dtypes(include=['float64', 'int64']).columns
        if len(numeryczne_kolumny) >= 2:
            kolumna_x = st.selectbox('Wybierz kolumnę dla osi X:', numeryczne_kolumny)
            kolumna_y = st.selectbox('Wybierz kolumnę dla osi Y:', numeryczne_kolumny)
            
            typ_wykresu = st.selectbox(
                'Wybierz typ wykresu:',
                ['Punktowy', 'Liniowy', 'Słupkowy']
            )

            if typ_wykresu == 'Punktowy':
                fig = px.scatter(df, x=kolumna_x, y=kolumna_y)
            elif typ_wykresu == 'Liniowy':
                fig = px.line(df, x=kolumna_x, y=kolumna_y)
            else:
                fig = px.bar(df, x=kolumna_x, y=kolumna_y)

            st.plotly_chart(fig)
        else:
            st.warning("Niewystarczająca liczba kolumn numerycznych do wizualizacji")

if __name__ == "__main__":
    main() 