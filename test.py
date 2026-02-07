import csv
import subprocess

def main():
    try:
        with open('pizza.csv', 'a', newline='') as csvfile:
            field_names = ['yeast_amount_tsp', 'rest_time_before_fridge_hours', 'ball_tightness', 'time_in_fridge_days', 'bake_day_sit_time_hours', 'bake_day_sit_method', 'ball_folds', 'bake_day_reball', 'result_texture', 'result_chewiness', 'result_oven_spring', 'result_overall', 'notes']
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            row_data = {field: input(f"Enter {field}: ") for field in field_names}
            
            writer.writerow(row_data)
            
            subprocess.run(['git', 'add', 'pizza.csv'], check=True)
            subprocess.run(['git', 'commit', '-m', 'Add pizza data entry'], check=True)
            subprocess.run(['git', 'push', 'origin', 'main'], check=True)
            
    except KeyboardInterrupt:
        print("\nEntry cancelled.")

if __name__ == "__main__":
    main()
