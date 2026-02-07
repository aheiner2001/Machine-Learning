import csv
with open('pizza.csv','a', newline='') as csvfile:

    field_names = [ 'yeast_amount_tsp', 'rest_time_before_fridge_hours','ball_tightness', 'time_in_fridge_days', 'bake_day_sit_time_hours', 'bake_day_sit_method', 'ball_folds',  'bake_day_reball', 'result_texture', 'result_chewiness', 'result_oven_spring', 'result_overall', 'notes']
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    row_data = {}
    for field in field_names:
        row_data[field] = input(f"Enter {field}: ")
    writer.writerow(row_data)


        # this is from the git branch test
        
