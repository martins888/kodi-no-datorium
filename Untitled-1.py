computer_turn = input("Enter computer turn: ").lower()
human_turn = input("Enter human turn: ").lower()
print(f"Kompis: {computer_turn} VS. Vecis: {human_turn}")

if computer_turn == human_turn:
    print("neizšķ.")

elif ((computer_turn == "paper" and human_turn == "rock") or 
        (computer_turn == "scissors" and human_turn == "paper") or 
        (computer_turn == "rock" and human_turn == "scissors")):
    print("Kompis uzvar")

else:
    print("Vecis uzvar")