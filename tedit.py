class Environment:
    LibInfo = {
        "name": "TEDIT",
        "credits": ["Charlie T"],
        "version": 1.0,
        "reqVersion": 1.3,
        "description": "A minimal NANO-like text editor with a clean TUI",
        "helpinfo": "tedit [filename] (filename not needed, unless you want to save your file.)"
    }

    import libload as lib
    global libs, system
    libs = lib.load_libs()
    system = libs["system"]

    def RunFromEnv(func):
        import keyboard
        import os

        content = []
        cursor_pos = 0
        filename = None
        status_msg = ""

        def top(text):
            (width, _) = os.get_terminal_size()
            pad = max(0, width - len(text))
            print(system.Output.Format.RESET, end="")
            print("\033[7m" + " " * (pad // 2) + text + " " * (pad - pad // 2) + "\033[0m")

        def bottom(text):
            (width, height) = os.get_terminal_size()
            pad = max(0, width - len(text))
            print(f"\033[{height-1};1H\033[7m" +
                " " * (pad // 2) + text + " " * (pad - pad // 2) +
                "\033[0m")

        def clear():
            os.system('cls' if os.name == 'nt' else 'clear')

        def load_file(path):
            nonlocal content, cursor_pos, status_msg
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = list(f.read())
                cursor_pos = 0
                status_msg = f"Opened: {path}"
            except Exception as e:
                status_msg = f"Failed to open file: {e}"

        def save_file():
            nonlocal status_msg
            if not filename:
                status_msg = "No filename!"
                return
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write("".join(content))
                status_msg = f"Saved: {filename}"
            except Exception as e:
                status_msg = f"Save failed: {e}"

        def display_content():
            clear()
            top(f"TEDIT | {cursor_pos}/{len(content)} | {filename or 'NEW'}")

            text = ''.join(content)
            if cursor_pos < len(text):
                before = text[:cursor_pos]
                cursor_char = text[cursor_pos]
                after = text[cursor_pos + 1:]
                print(f"{before}\x1b[7m{cursor_char}\x1b[0m{after}")
            else:
                print(f"{text}\x1b[7m \x1b[0m")

            bottom(status_msg or "Ctrl+S Save | Ctrl+O Reload | Esc Exit")

        def get_line_col(pos):
            """Get the line number and column position for a given cursor position"""
            text = ''.join(content[:pos])
            lines = text.split('\n')
            line = len(lines) - 1
            col = len(lines[-1])
            return line, col

        def get_pos_from_line_col(line, col):
            """Get cursor position from line and column"""
            text = ''.join(content)
            lines = text.split('\n')
            
            # Clamp line to valid range
            line = max(0, min(line, len(lines) - 1))
            
            # Calculate position up to the start of the target line
            pos = sum(len(lines[i]) + 1 for i in range(line))
            
            # Add column offset, clamped to line length
            pos += min(col, len(lines[line]))
            
            return pos

        def on_key_press(event):
            nonlocal cursor_pos, status_msg, content, filename

            if event.name == 'esc':
                return False

            if keyboard.is_pressed('ctrl'):
                if event.name == 's': save_file()
                elif event.name == 'o' and filename:
                    load_file(filename)
                elif event.name == 'n':
                    keyboard.unhook_all()  # Unhook keyboard
                    clear()
                    print("\033[?25h")  # Show cursor
                    new_filename = input("Filename: ")
                    print("\033[?25l")  # Hide cursor
                    if new_filename.strip():
                        filename = new_filename
                        status_msg = f"Filename set: {filename}"
                    keyboard.on_press(on_key_press)  # Re-hook keyboard
                display_content()
                return

            if event.name == 'left' and cursor_pos > 0:
                cursor_pos -= 1
            elif event.name == 'right' and cursor_pos < len(content):
                cursor_pos += 1
            elif event.name == 'up':
                line, col = get_line_col(cursor_pos)
                if line > 0:
                    cursor_pos = get_pos_from_line_col(line - 1, col)
            elif event.name == 'down':
                line, col = get_line_col(cursor_pos)
                text = ''.join(content)
                max_line = len(text.split('\n')) - 1
                if line < max_line:
                    cursor_pos = get_pos_from_line_col(line + 1, col)
            elif event.name == 'backspace' and cursor_pos > 0:
                content.pop(cursor_pos - 1)
                cursor_pos -= 1
            elif event.name == 'delete' and cursor_pos < len(content):
                content.pop(cursor_pos)
            elif event.name == 'enter':
                content.insert(cursor_pos, '\n')
                cursor_pos += 1
            elif event.name == 'space':
                content.insert(cursor_pos, ' ')
                cursor_pos += 1
            elif len(event.name) == 1:
                char = event.name
                if keyboard.is_pressed('shift') and char.isalpha():
                    char = char.upper()
                content.insert(cursor_pos, char)
                cursor_pos += 1

            display_content()

        def main():
            nonlocal filename

            if len(func) != 0:
                filename = func[0]
                load_file(filename)

            try:
                print("\033[?25l")
                display_content()
                keyboard.on_press(on_key_press)
                keyboard.wait('esc')
            finally:
                keyboard.unhook_all()
                print("\033[?25h")
                print(system.Output.Format.LIB_RESET)
                clear()

        main()

if __name__ == "__main__":
    print("This file cannot run without the Environment.")