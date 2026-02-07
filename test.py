import csv
with open('pizza.csv','w', newline='') as csvfile:

    field_names = ['date','time_in_fridge_days','rest_time_before_fridge_hours','yeast_amount_tsp','bake_day_sit_time_hours','bake_day_sit_method','bake_day_reball','ball_folds','ball_tightness','notes','result_texture','result_chewiness','result_oven_spring','result_overall']
    writer = csv.DictWriter(csvfile, fieldnames=field_names)

    writer.writeheader()
    row_data = {}
    for field in field_names:
        row_data[field] = input(f"Enter {field}: ")
    writer.writerow(row_data)


        # this is from the git branch test
        
