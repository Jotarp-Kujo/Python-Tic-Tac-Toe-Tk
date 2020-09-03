from time import sleep
print("Scrivi 'quit' per uscire")
# ----- Global Variables -----

# board di default
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

# se il gioco è ancora in esecuzione
gioco_in_esecuzione = True

# chi ha vinto? o pareggiato?
vincitore = None

# è il turno di?
giocatore_corrente = "X"


def mostra_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def gioca():
    # Mostra la board di default
    mostra_board()

    while gioco_in_esecuzione:
        gestisci_turni(giocatore_corrente)

        # Controlla se il gioco è finito
        controlla_se_gioco_finito()

        # Passa il turno all'altro giocatore
        flip_player()

    # il gioco è finito
    if vincitore == "X" or vincitore == "O":
        print("Il giocatore " + vincitore + " ha vinto!")
    elif vincitore is None:
        print("E abbiamo un pareggio!!")


def gestisci_turni(player):

    print("È il turno del giocatore " + player)
    posizione = input("Scegli una posizione tra 1-9: ")
    if posizione == "quit":
        print("Ok,chiudo il programma")
        sleep(1)
        exit()

    valid = False
    while not valid:

        while posizione not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            posizione = input("Posizione non valida,scegli una posizione tra 1-9: ")
            if posizione == "quit":
                print("Ok,chiudo il programma")
                sleep(1)
                exit()

        posizione = int(posizione) - 1

        if board[posizione] == "-":
            valid = True
        else:
            print("Quella casella è già occupata,scegline un'altra")

    board[posizione] = player

    mostra_board()


def controlla_se_gioco_finito():
    controlla_se_vittoria()
    controlla_se_pareggio()


def controlla_se_vittoria():

    global vincitore

    # controlla righe
    tris_riga = check_rows()
    # controlla colonne
    tris_colonna = check_columns()
    # controlla diagonali
    tris_diagonale = check_diagonals()
    if tris_riga:
        vincitore = tris_riga
    elif tris_colonna:
        vincitore = tris_colonna
    elif tris_diagonale:
        vincitore = tris_diagonale
    else:
        vincitore = None
    return


def check_rows():
    global gioco_in_esecuzione
    riga_1 = board[0] == board[1] == board[2] != "-"
    riga_2 = board[3] == board[4] == board[5] != "-"
    riga_3 = board[6] == board[7] == board[8] != "-"
    if riga_1 or riga_2 or riga_3:
        gioco_in_esecuzione = False
    if riga_1:
        return board[0]
    elif riga_2:
        return board[3]
    elif riga_3:
        return board[6]
    return


def check_columns():
    global gioco_in_esecuzione
    colonna_1 = board[0] == board[3] == board[6] != "-"
    colonna_2 = board[1] == board[4] == board[7] != "-"
    colonna_3 = board[2] == board[5] == board[8] != "-"
    if colonna_1 or colonna_2 or colonna_3:
        gioco_in_esecuzione = False
    if colonna_1:
        return board[0]
    elif colonna_2:
        return board[1]
    elif colonna_3:
        return board[2]
    return


def check_diagonals():
    global gioco_in_esecuzione
    diagonale_1 = board[6] == board[4] == board[2] != "-"
    diagonale_2 = board[8] == board[4] == board[0] != "-"
    if diagonale_1 or diagonale_2:
        gioco_in_esecuzione = False
    if diagonale_1:
        return board[0]
    elif diagonale_2:
        return board[6]
    return


def controlla_se_pareggio():
    return


def flip_player():
    global giocatore_corrente
    if giocatore_corrente == "X":
        giocatore_corrente = "O"
    elif giocatore_corrente == "O":
        giocatore_corrente = "X"
    return


gioca()
