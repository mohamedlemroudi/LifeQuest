from rich.console import Console

class UI:
    def __init__(self):
        self.console = Console()

    def show_initial_menu(self):
        print("====================")
        print("     LIFEQUEST")
        print("====================")
        print("1. Iniciar sesión")
        print("2. Crear jugador")
        print("0. Salir")

    def ask_initial_choice(self):
        while True:
            try:
                initial_choice = int(input("Elige una opción: "))
                if initial_choice in (1,2):
                    return initial_choice
                
                elif initial_choice == 0:
                    print("Salir del programa.")
                    return initial_choice
                
                else:
                    self.console.print("[bold red]No existe esta opcion.[/bold red]")
            except ValueError:
                self.console.print("[bold red]Respuesta no válida.[/bold red]")

    def show_menu(self):
        print("====================")
        print("     LIFEQUEST")
        print("====================")
        print("1. Ver jugador")
        print("2. Completar misión")
        print("3. Ver estadísticas")
        print("0. Salir")

    def show_player(self, player):
        print("Jugador: " + player.name)
        print("Nivel: " + str(player.level))
        print("XP: " + str(player.xp))
        print("Misiones completadas: " + str(player.missions_completed))
        print("XP total: " + str(player.total_xp))

    def show_stats(self, player):
            print(f"Jugador: {player.name}")
            print(f"Nivel: {player.level}")
            print(f"XP actual: {player.xp}")
            print(f"XP total: {player.total_xp}")
            print(f"Misiones completadas: {player.missions_completed}")
    
            if player.missions_completed > 0:
                average_xp = player.total_xp / player.missions_completed
            else:
                average_xp = 0
    
            print(f"XP media por misión: {average_xp}")

    def show_missions(self, missions):
        for position, mission in enumerate(missions, 1):
            print(
                f"{position}. {mission.name} | "
                f"{mission.difficulty} | "
                f"+{mission.calculate_reward()} XP | "
                f"{mission.days_left} days left"
            )

        print("0. Volver al menú principal.")


    def ask_missions(self):
        try:
            return int(input("Elige una misión: "))

        except ValueError:
            self.console.print("[bold red]Respuesta no válida.[/bold red]")


    def ask_options_menu(self):
        try:
            choice = int(input("Elige una opción: "))

            if choice in (1, 2, 3):
                return choice
            
            elif choice == 0:
                print("Saliendo del juego.")
                return choice

            else:
                self.console.print("[bold red]Opción no válida. Por favor, elige otra opción.[/bold red]")
                return -1

        except ValueError:
            self.console.print("[bold red]Respuesta no válida.[/bold red]")


    def ask_player_name(self):
        return input("Introduce el nombre del jugadora: ")

    def show_result_login(self, answer):
        if answer:
            self.console.print("[bold green]Login CORRECT![/bold green]")
        else:
            self.console.print("[bold red]Login INCORRECT![/bold red]")


    def show_result_singin(self, answer):
        if answer:
            self.console.print("[bold green]Se ha creado el jugador![/bold green]")
        else:
            self.console.print("[bold red]El jugador ja existe.[/bold red]")

    def show_mission_completed(self, mission_name, reward):
        self.console.print(f"[bold green]Has completado: {mission_name}[/bold green]")
        self.console.print(f"[bold green]Has ganado {reward} XP.[/bold green]")

    def not_found_mission(self):
        self.console.print("[bold red]No existe esa misión.[/bold red]")
    
    def incorrect_name(self):
        self.console.print("[bold red]No és un nombre correcto, por favor introduce otro nombre.[/bold red]")

     