from tkinter import *
import os
import helper
import constants

dictionary_squares = constants.DICTIONARY_INIT


class Creator:

    def __init__(self):
        self.folder_place = os.getcwd()
        self.index = 0
        self.helper = helper.Helper()

    def change_label(self, text_name1, text_name2, number):
        if number == 1:
            win_label['text'] = ""
            win_label.pack_forget()
            win_label.config(text=text_name1)
        else:
            win_label['text'] = ""
            win_label.pack_forget()
            win_label.config(text=text_name2)

    def insert_name_into_label(self):
        label_player1.config(text=str(player_name1.get()))
        label_player2.config(text=str(player_name2.get()))
        submit_button["state"] = DISABLED
        submit_button["bg"] = "#AFAFA4"
        player_name1["state"] = DISABLED
        player_name2["state"] = DISABLED
        label_player1["bg"] = "#27D239"
        label_player1["fg"] = "#CB7B26"

    def insert_symbol(self, entry, square_number, result_value):
        text_game_ok = "GAME ON"
        text_position_occupied = "POSITION IS ALREADY OCCUPIED"
        global turn
        global text_var
        text_var = StringVar()
        dictionary_analogy_squares = {1: square1, 2: square2, 3: square3, 4: square4, 5: square5, 6: square6,
                                      7: square7, 8: square8, 9: square9}
        win_label.grid(row=3, columnspan=3)
        win_label.pack_forget()
        turn_player = helper.Helper.get_player_turn(dictionary_squares)
        print("Player turn: ", turn_player)
        if turn_player:
            # first make the second player like default
            label_player2["bg"] = "#E4E4D6"
            label_player2["fg"] = "#C03964"
            label_player1["bg"] = "#27D239"
            label_player1["fg"] = "#CB7B26"
            if square_number == 1:
                # setting the exact self.index
                win_label.pack_forget()
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player1["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, 'end')
                    entry.insert(0, "0")
                    result_value.set("0")
                    dictionary_squares.update({1: "0"})

            elif square_number == 2:
                win_label.pack_forget()
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player1["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, 'end')
                    entry.insert(0, "0")
                    result_value.set("0")
                    dictionary_squares.update({2: "0"})

            elif square_number == 3:
                win_label.pack_forget()
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player1["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    win_label.config(text=text_game_ok)
                    entry.delete(0, 'end')
                    entry.insert(0, "0")
                    result_value.set("0")
                    dictionary_squares.update({3: "0"})

            elif square_number == 4:
                win_label.pack_forget()
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player1["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, 'end')
                    entry.insert(0, "0")
                    result_value.set("0")
                    dictionary_squares.update({4: "0"})

            elif square_number == 5:
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player1["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, 'end')
                    entry.insert(0, "0")
                    result_value.set("0")
                    dictionary_squares.update({5: "0"})

            elif square_number == 6:
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player1["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, END)
                    entry.insert(0, "0")
                    result_value.set("0")
                    dictionary_squares.update({6: "0"})

            elif square_number == 7:
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player1["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, END)
                    entry.insert(0, "0")
                    result_value.set("0")
                    dictionary_squares.update({7: "0"})

            elif square_number == 8:
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player1["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, END)
                    entry.insert(0, "0")
                    result_value.set("0")
                    dictionary_squares.update({8: "0"})

            else:
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player1["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, END)
                    entry.insert(0, "0")
                    result_value.set("0")
                    dictionary_squares.update({9: "0"})

        else:
            # first make the first second player like default
            label_player1["bg"] = "#E4E4D6"
            label_player1["fg"] = "#C03964"
            label_player2["bg"] = "#27D239"
            label_player2["fg"] = "#CB7B26"
            if square_number == 1:
                win_label.pack_forget()
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED"
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player2["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, 'end')
                    entry.insert(0, "X")
                    result_value.set("X")
                    dictionary_squares.update({1: "X"})

            elif square_number == 2:
                win_label.pack_forget()
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player2["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, 'end')
                    entry.insert(0, "X")
                    result_value.set("X")
                    dictionary_squares.update({2: "X"})

            elif square_number == 3:
                win_label.pack_forget()
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player2["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, 'end')
                    entry.insert(0, "X")
                    result_value.set("X")
                    dictionary_squares.update({3: "X"})

            elif square_number == 4:
                win_label.pack_forget()
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player2["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, END)
                    entry.insert(0, "X")
                    result_value.set("X")
                    dictionary_squares.update({4: "X"})

            elif square_number == 5:
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player2["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, END)
                    entry.insert(0, "X")
                    result_value.set("X")
                    dictionary_squares.update({5: "X"})

            elif square_number == 6:
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player2["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, END)
                    entry.insert(0, "X")
                    result_value.set("X")
                    dictionary_squares.update({6: "X"})

            elif square_number == 7:
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player2["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, END)
                    entry.insert(0, "X")
                    result_value.set("X")
                    dictionary_squares.update({7: "X"})

            elif square_number == 8:
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player2["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, END)
                    entry.insert(0, "X")
                    result_value.set("X")
                    dictionary_squares.update({8: "X"})

            else:
                if helper.Helper.check_number(square_number, dictionary_squares):
                    # partial(self.change_label, inner_frame, "POSITION ALREADY OCCUPIED")
                    self.change_label(text_position_occupied, text_game_ok, 1)
                    label_player2["bg"] = "#E4E4D6"
                else:
                    self.change_label(text_position_occupied, text_game_ok, 2)
                    entry.delete(0, END)
                    entry.insert(0, "X")
                    result_value.set("X")
                    dictionary_squares.update({9: "X"})
        print(dictionary_squares)
        # print(self.available_values)

        '''check for winner'''
        return_code, list_winner_squares = self.helper.define_winner(dictionary_squares)
        if return_code == 1:
            # this means player1 has won
            win_label['text'] = ""
            win_label.pack_forget()
            player1_name = str(player_name1.get()).upper()
            win_label["text"] = player1_name + constants.ENDING_MESSAGE1
            # extract elements and make the winner
            dictionary_analogy_squares[list_winner_squares[0]]["bg"] = "#27D239"
            dictionary_analogy_squares[list_winner_squares[1]]["bg"] = "#27D239"
            dictionary_analogy_squares[list_winner_squares[2]]["bg"] = "#27D239"
            dictionary_analogy_squares[list_winner_squares[0]]["fg"] = "#F6F61C"
            dictionary_analogy_squares[list_winner_squares[1]]["fg"] = "#F6F61C"
            dictionary_analogy_squares[list_winner_squares[2]]["fg"] = "#F6F61C"
            label_player1["bg"] = "#E4E4D6"
            label_player2["bg"] = "#E4E4D6"
            win_label["bg"] = "#27D239"

        if return_code == 2:
            # this means player2 has won
            win_label['text'] = ""
            win_label.pack_forget()
            player2_name = str(player_name2.get()).upper()
            win_label["text"] = player2_name + constants.ENDING_MESSAGE1
            # extract elements and make the winner
            dictionary_analogy_squares[list_winner_squares[0]]["bg"] = "#27D239"
            dictionary_analogy_squares[list_winner_squares[1]]["bg"] = "#27D239"
            dictionary_analogy_squares[list_winner_squares[2]]["bg"] = "#27D239"
            dictionary_analogy_squares[list_winner_squares[0]]["fg"] = "#F6F61C"
            dictionary_analogy_squares[list_winner_squares[1]]["fg"] = "#F6F61C"
            dictionary_analogy_squares[list_winner_squares[2]]["fg"] = "#F6F61C"
            label_player1["bg"] = "#E4E4D6"
            label_player2["bg"] = "#E4E4D6"
            win_label["bg"] = "#27D239"

        if return_code == 3:
            win_label['text'] = ""
            win_label.pack_forget()
            win_label["text"] = constants.ENDING_MESSAGE2
            label_player1["bg"] = "#E4E4D6"
            label_player2["bg"] = "#E4E4D6"
            square1["bg"] = "#BFD0ED"
            square2["bg"] = "#BFD0ED"
            square3["bg"] = "#BFD0ED"
            square4["bg"] = "#BFD0ED"
            square5["bg"] = "#BFD0ED"
            square6["bg"] = "#BFD0ED"
            square7["bg"] = "#BFD0ED"
            square8["bg"] = "#BFD0ED"
            square9["bg"] = "#BFD0ED"
            win_label["bg"] = "#BFD0ED"

    def create_outform(self, window_place):
        window_place.title("Tic Tac Toe Game")
        window_place.geometry("1050x700")
        icon_name = os.path.join(os.getcwd(), r"files\140-1404273_tic-tac-toe-toe-tic-tac-play-comments.ico")
        window_place.iconbitmap(icon_name)
        window_place.configure(background="#A0CFEC")

    def create_inform(self, window_place):
        global square1
        global square2
        global square3
        global square4
        global square5
        global square6
        global square7
        global square8
        global square9
        global win_label
        global list_squares
        global label_value
        global player_name1
        global player_name2
        global label_player1
        global label_player2
        global submit_button

        # we use this to keep and to store where x is marked
        result_square = StringVar()
        label_value = StringVar()
        label_value.set("GAME ON")

        configuration_frame = LabelFrame(window_place, text="CONFIGS", bg="#110C44", fg="#9FE51C",
                                         font=("Comic Sans", 20, "bold"), labelanchor="n", width="500", cursor="arrow",
                                         height=200, padx=100, pady=25)
        configuration_frame.grid(row=0, column=0, )  # put it in the middle
        configuration_frame.rowconfigure(0, weight=1)
        configuration_frame.columnconfigure(0, weight=1)
        player_name1 = Entry(configuration_frame, fg="#DA8891", bg="#E6D8EA", font=("Comic Sans", 11, "bold"), bd=3,
                             cursor="target", width=20, justify="center", )
        player_name2 = Entry(configuration_frame, fg="#DA8891", bg="#E6D8EA", font=("Comic Sans", 11, "bold"), bd=3,
                             cursor="target", width=20, justify="center", )
        submit_button = Button(configuration_frame, fg="#383911", bg="#D3D68A", font=("Comic Sans", 15, "bold"), bd=3,
                               cursor="target", width=10, justify="center", text="SUBMIT",
                               command=lambda: self.insert_name_into_label())
        label_player1 = Label(configuration_frame, fg="#C03964", bg="#E4E4D6", font=("Comic Sans", 11, "bold"), bd=7,
                              cursor="spraycan", width=15, justify="center", text="")
        label_player2 = Label(configuration_frame, fg="#C03964", bg="#E4E4D6", font=("Comic Sans", 11, "bold"), bd=7,
                              cursor="spraycan", width=15, justify="center", text="")
        player_name1.insert(0, "Name player1")
        player_name2.insert(0, "Name player2")
        player_name1.grid(row=0, column=0, sticky="", padx=10)
        player_name1.rowconfigure(1, weight=1)
        player_name1.columnconfigure(1, weight=1)
        player_name2.grid(row=1, column=0, sticky="", padx=10)
        player_name2.rowconfigure(1, weight=1)
        player_name2.columnconfigure(1, weight=1)
        submit_button.grid(pady=15, row=2, column=0, padx=10, sticky=W + E, columnspan=2,
                           )
        submit_button.rowconfigure(1, weight=1)
        submit_button.columnconfigure(1, weight=1)
        label_player1.grid(row=3, column=0, padx=25, pady=20)
        label_player2.grid(row=3, column=1, padx=25, pady=20)

        # create a frame
        width_frame = 300
        height_frame = 400
        inner_frame = LabelFrame(window_place, text="TIC TAC TOE GAME", bg="#110C44", fg="#9FE51C",
                                 font=("Comic Sans", 20, "bold"), labelanchor="n", width="300", cursor="pirate",
                                 height=400)
        inner_frame.grid(padx=width_frame / 2, pady=height_frame / 3, row=1, column=0, )  # put it in the middle
        inner_frame.grid_rowconfigure(0, weight=1)
        inner_frame.grid_columnconfigure(0, weight=1)
        square1 = Entry(inner_frame, fg="#C03964", bg="#D2DF8E", font=("Comic Sans", 20, "bold"), bd=6,
                        cursor="spraycan", width=15, justify="center", )
        square2 = Entry(inner_frame, fg="#C03964", bg="#D2DF8E", font=("Comic Sans", 20, "bold"), bd=6,
                        cursor="spraycan", width=15, justify="center", )
        square3 = Entry(inner_frame, fg="#C03964", bg="#D2DF8E", font=("Comic Sans", 20, "bold"), bd=6,
                        cursor="spraycan", width=15, justify="center", )
        square4 = Entry(inner_frame, fg="#C03964", bg="#D2DF8E", font=("Comic Sans", 20, "bold"), bd=6,
                        cursor="spraycan", width=15, justify="center", )
        square5 = Entry(inner_frame, fg="#C03964", bg="#D2DF8E", font=("Comic Sans", 20, "bold"), bd=6,
                        cursor="spraycan", width=15, justify="center", )
        square6 = Entry(inner_frame, fg="#C03964", bg="#D2DF8E", font=("Comic Sans", 20, "bold"), bd=6,
                        cursor="spraycan", width=15, justify="center", )
        square7 = Entry(inner_frame, fg="#C03964", bg="#D2DF8E", font=("Comic Sans", 20, "bold"), bd=6,
                        cursor="spraycan", width=15, justify="center", )
        square8 = Entry(inner_frame, fg="#C03964", bg="#D2DF8E", font=("Comic Sans", 20, "bold"), bd=6,
                        cursor="spraycan", width=15, justify="center", )
        square9 = Entry(inner_frame, fg="#C03964", bg="#D2DF8E", font=("Comic Sans", 20, "bold"), bd=6,
                        cursor="spraycan", width=15, justify="center", )
        win_label = Label(inner_frame, text="GAME ON", fg="#C03964", bg="#D2DF8E", font=("Comic Sans", 24, "bold"),
                          bd=3)

        # put squares on grid
        square1.grid(row=0, column=0, )
        square2.grid(row=0, column=1, )
        square3.grid(row=0, column=2, )
        square4.grid(row=1, column=0, )
        square5.grid(row=1, column=1, )
        square6.grid(row=1, column=2, )
        square7.grid(row=2, column=0, )
        square8.grid(row=2, column=1, )
        square9.grid(row=2, column=2, )
        square1.bind("<1>", lambda event, entry=square1: self.insert_symbol(entry, 1, result_square))
        square2.bind("<1>", lambda event, entry=square2: self.insert_symbol(entry, 2, result_square))
        square3.bind("<1>", lambda event, entry=square3: self.insert_symbol(entry, 3, result_square))
        square4.bind("<1>", lambda event, entry=square4: self.insert_symbol(entry, 4, result_square))
        square5.bind("<1>", lambda event, entry=square5: self.insert_symbol(entry, 5, result_square))
        square6.bind("<1>", lambda event, entry=square6: self.insert_symbol(entry, 6, result_square))
        square7.bind("<1>", lambda event, entry=square7: self.insert_symbol(entry, 7, result_square))
        square8.bind("<1>", lambda event, entry=square8: self.insert_symbol(entry, 8, result_square))
        square9.bind("<1>", lambda event, entry=square9: self.insert_symbol(entry, 9, result_square))

    def run_gui(self):
        root = Tk()
        self.create_outform(root)
        self.create_inform(root)
        root.mainloop()
