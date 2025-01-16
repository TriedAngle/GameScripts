#!/usr/bin/env python3
import argparse
from collections import deque
from typing import List, Optional

def find_path(
    start: int,
    target: int,
    options: List[int],
    required_sequence: Optional[List[int]] = None
) -> Optional[List[int]]:
    """
    Find the shortest path from start to target using given options.
    Optionally enforce a specific sequence of final steps.
    
    Args:
        start: Starting value
        target: Target value to reach
        options: List of available operations (can be positive or negative)
        required_sequence: Optional list of operations that must be used in order at the end
    
    Returns:
        List of operations to reach target, or None if no solution exists
    """
    options = sorted(options)
    min_op = min(options)
    max_op = max(options)
    
    def can_reach_target(current: int, remaining_steps: int) -> bool:
        """Check if it's theoretically possible to reach target within steps."""
        if current == target:
            return True
        
        if current < target:
            max_possible = current + (max_op * remaining_steps)
            return max_possible >= target
        
        min_possible = current + (min_op * remaining_steps)
        return min_possible <= target

    if start == target:
        return []
    
    min_step_size = min(abs(op) for op in options)
    initial_min_steps = abs(target - start) // min_step_size
    max_steps = min(20, initial_min_steps * 2)  # Use initial_min_steps to set a better bound
    
    queue = deque([(start, [], max_steps)])
    seen = {start: 0}  # value -> shortest path length to reach it
    
    intermediate_target = target
    if required_sequence:
        required_steps = len(required_sequence)
        max_steps = min(max_steps, initial_min_steps + required_steps)
        for op in required_sequence[::-1]:
            intermediate_target -= op
    
    while queue:
        current_value, path, steps_left = queue.popleft()
        current_len = len(path)
        
        if not can_reach_target(current_value, steps_left):
            continue
            
        if current_value in seen and seen[current_value] < current_len:
            continue
        
        for option in options:
            new_value = current_value + option
            new_path = path + [option]
            
            if new_value in seen and seen[new_value] <= len(new_path):
                continue
                
            distance_to_target = abs(target - new_value)
            if required_sequence:
                distance_to_intermediate = abs(intermediate_target - new_value)
                if distance_to_intermediate > (steps_left - 1) * max(abs(min_op), abs(max_op)):
                    continue
            elif distance_to_target > steps_left * max(abs(min_op), abs(max_op)):
                continue
            
            if len(new_path) > max_steps:
                continue
            
            if required_sequence:
                if new_value == intermediate_target:
                    return new_path + required_sequence
            elif new_value == target:
                return new_path
            
            queue.append((new_value, new_path, steps_left - 1))
            seen[new_value] = len(new_path)
    
    return None

def main():
    parser = argparse.ArgumentParser(description='Find shortest path to target value using given operations')
    parser.add_argument('target', type=int, help='Target value to reach')
    parser.add_argument('--start', type=int, default=0, help='Starting value (default: 0)')
    parser.add_argument('--options', type=int, nargs='+',
                      default=[-3, -6, -5, -15, 2, 7, 13, 16],
                      help='List of available operations (default: -3 -6 -5 -15 2 7 13 16)')
    parser.add_argument('--required', type=int, nargs='+',
                      help='Sequence of operations that must be used in order at the end')
    
    args = parser.parse_args()
    
    path = find_path(args.start, args.target, args.options, args.required)
    
    if path is None:
        print(f"No solution found to reach {args.target} from {args.start}")
    else:
        print(f"Path found with {len(path)} steps:")
        current = args.start
        print(f"Start: {current}")
        for i, step in enumerate(path, 1):
            current += step
            print(f"Step {i}: {step:+d} -> {current}")

if __name__ == "__main__":
    main()
