def format_table(headers, rows):
    # Determine column widths
    col_widths = [max(len(str(item)) for item in col) for col in zip(*[headers] + rows)]
    
    # Create format string
    format_str = " | ".join([f"{{:<{width}}}" for width in col_widths])
    
    # Create table
    table = []
    table.append(format_str.format(*headers))
    table.append("-+-".join(['-' * width for width in col_widths]))
    for row in rows:
        table.append(format_str.format(*row))
    
    return "\n".join(table)