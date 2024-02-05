# ShortMaker
PL

Program służy do masowego generowania krótkich treści (shorts) z głosem lektora, muzyką i dynamicznym tłem. Fakty implementowane są do video z pliku csv. Video w tle wybierane jest przez użytkownika który może podać ścieżkę do dłuższego filmu i wybrać jego część do dalszej edycji.

Sposób użycia:
Jeśli zależy nam na wydajności i czasie w SampleMaker wprowadzić ścieżkę do dłuższego filmu oraz porządany czas trwania tak aby wygenerować plik (sampel) który będzie łatwiejszy do edycji przez główny program
Zmienić przykładowe fakty w pliku Fakty.csv 
W TitleFormater.py zmienić ścieżkę do pobranych plików.
Uruchomić MainProgram z odpowiednia nazwa sampla lub dłuższego pliku, nazwą ścieżki audio, nazwą kanału, która będzie widoczna na shortsie. Przykładowe parametry widnieją w kodzie, co za tym idzie, po odpaleniu MainProgram powinien zostać wygenerowany przykładowy short na podstawie załączonych plików.


Biblioteki niezbędne do działania programu:
moviepy 
Csv
Selenium
Pyautogui
Pyperclip

