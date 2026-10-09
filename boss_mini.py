# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

p_hp = 50
b_hp = 50

# Remove SECRET_CODE, see below in the game loop for updating the input screen
SECRET_CODE = "ADMIN_ACCESS_2025"
# Add MAX_HP to allow for a maximum p_hp value
MAX_HP = 50

# Add b_hp and subtract from the bosses HP, also check for if below 0
def attack():
    global b_hp
    b_hp -= 10
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")

# Check for overheal and healing while dead
def heal():
    global p_hp
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return
    p_hp += 20
    if p_hp > MAX_HP:
        p_hp = MAX_HP
    print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
    print(f"\nPlayer: {p_hp} | Boss: {b_hp}")

    # Remove "[c]heat: and change grammar accordingly."
    choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()

    if choice == 'a':
        attack()
    elif choice == 'h':
        heal()

    # Remove this elif statemnt
    elif choice == 'c':
        if input("Code: ") == SECRET_CODE:
            b_hp = 0
    # Remove 'c' from this as well
    else:
        print("Invalid choice! Please choose 'a', 'h', or 'c'.")

    if b_hp <= 0:
        print("Victory!")
        break

    if b_hp > 0:
        p_hp -= 10

print("Game Over!")
