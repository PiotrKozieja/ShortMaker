def format_text(text, max_chars):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line + word) <= max_chars:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    if current_line:
        lines.append(current_line.strip())

    return '\n'.join(lines)

