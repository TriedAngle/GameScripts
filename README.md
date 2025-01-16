# Game Scripts
My Game Scripts

## TFC Anvil
A script that finds the shortest sequence of operations to reach the target value with an optional required ending sequence. Made for Terrafirmacraft's Anvil recipes and already has the options as default.

### Usage
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
