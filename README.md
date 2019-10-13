# robocik_rekrutacja

Zadanie rekrutacyjne:

    W łodzi podwodnej większość komponentów ma swój własny skrypt zarządzający.
    Większość z nich musi komunikować się z co najmniej jednym, innym skryptem.
    
    Mając załączone szkice 3 programów "*.py", zaimplementuj klasę "Client", która pozwoli na podobną komunikację.
    "Program_B" ma wysyłać jedną zmienną typu całkowitego do "Program_A".
    "Program_C" ma wysyłać słownik "pos_dict" i odbierać "received_dict" od "Program_A".
    "Program_A" ma odbierać zmienną całkowitą od "Program_B", odbierać słownik "pos_dict" od "Program_C", a następnie wysyłać słownik do "Program_C"
    Programy mają działać w pętli. 

    Wymagania implementacji:
        - klasa Client może pobierać dowolne argumenty podczas tworzenia, mogą być one spersonalizowane dla danego skryptu.
        - zarówno w czasie wysyłania jak i odbierania danych klasa Client może korzystać z następujących informacji: 
            * do którego skryptu ma wysłać / z którego ma odebrać dane
            * słówko kluczowe po którym można rozpoznać dane
        - zastosowane rozwiązanie powinno działać na Linuxie
        - można tworzyć dowolne pliki konfiguracyjne czy mapujące
        - można używać dowolnych narzędzi i rozwiązań pośredniczących, wymagana jednak jest instrukcja uruchomienia (lub modyfikacja skryptu /run.sh)

    
    Po zaimplementowaniu rozwiązania podaj co najmniej jedną zaletę swojego wyboru.
    Jeśli dostrzegasz, podaj też conajmniej jedną wadę. 
    W przypadku rozważania innej metody, uzasadnij krótko swój wybór.
    
    
    

      
     
            