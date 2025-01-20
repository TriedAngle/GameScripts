# Scripts
My Utility and Game Scripts

## Utility
### Rust Debug Pretty Printer
A CLI tool that pretty prints Rust Debug format output with customizable nesting depth. It properly indents nested structures and can collapse deeply nested content for better readability.

#### Usage
Basic usage:
```bash
# From stdin
./rust_debug_pretty.py

# From file
./rust_debug_pretty.py input.txt

# From pipe
echo "Debug{field: value}" | ./rust_debug_pretty.py
```

Options:
- `--max-depth` or `-d`: Maximum nesting depth before collapsing (default: 3)
- `--indent` or `-i`: Number of spaces for each indent level (default: 2)

Example with custom settings:
```bash
# Use 4-space indent and collapse after 2 levels
./rust_debug_pretty.py --max-depth 2 --indent 4 input.txt
```

## Game
### TFC Anvil
A script that finds the shortest sequence of operations to reach the target value with an optional required ending sequence. Made for Terrafirmacraft's Anvil recipes and already has the options as default.

#### Usage
Basic usage:
```bash
python path_finder.py TARGET
```

Example with specific requirements:
```bash
# Find path to 84, enforcing last steps as +16 then +2
python path_finder.py 84 --required 16 2
```

Options:
- `--start`: Starting value (default: 0)
- `--options`: List of available operations (default: -3 -6 -5 -15 2 7 13 16)
- `--required`: Sequence that must be used at the end of path

The script will display each step and the resulting value at each point in the path.
