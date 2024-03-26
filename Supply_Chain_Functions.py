import math
#........................................................................
#     This file consists of all the functions present in the library 
#........................................................................

def single_factor_productivity(input:int,output:int) -> float : #The function returns standard output per standard unit of input
    productivity = (output/input)
    return productivity
#......................................................................................................................
def multi_factor_productivity(output:int,*args:int) -> float: # The function returns standard output per standard unit of input
    final_input = 0
    for i in args: # iterating over all the input factors to get the sum 
        final_input +=i

    productivity = (output/final_input)
    return productivity
#......................................................................................................................
def moving_average(time_period:int,demand:list,index:int)->float: # returns the average of last n values 
    sum_values = 0 
    counter = 0 # keeps track of the time period 
    while time_period > 0:
        sum_values+= demand[index-1]
        time_period-=1
        counter +=1

    moving_average = (sum_values/counter)
    return moving_average
#......................................................................................................................
def weighted_moving_average(demand:list,weights:list,index:int):
    answer = 0 
    sum_weight = 0 # counts sum of weight to calculate the average 
    for weight in weights:
        index -=1
        sum_weight += weight
        answer += (demand[index] * weight) 

    weighted_moving_average = answer/sum_weight
    return weighted_moving_average
#......................................................................................................................
def forecast_error(actual_demand:float,forecast_value:float):
    forecast_error = (actual_demand - forecast_value)
    return forecast_error
#......................................................................................................................
def mean_absolute_deviation(actual:list,forecast:list,time_period:int,index:int) ->float:
    counter = 0 
    difference_sum = 0
    while time_period > 0:
        time_period -=1
        index -=1
        difference_sum += actual[index] - forecast[index]
        counter +=1

    mean_absolute_deviation = difference_sum/counter
    return mean_absolute_deviation
#......................................................................................................................
def mean_squared_error(index:int,actual_demand:list,forecasted_value:list,time_period:int)->float:
    square_sum = 0 
    counter = 0 
    while time_period > 0:
        time_period -=1
        index -=1
        counter +=1
        square_sum += forecast_error(actual_demand[index],forecasted_value[index])

    mean_squared_error = square_sum/counter
    return mean_squared_error
#......................................................................................................................
def utilization(actual_output:int,design_capacity:int)->float:
    utilization = (actual_output/design_capacity)
    return utilization
#......................................................................................................................
def efficiency(actual_output:int,effective_capacity:int)->float:
    efficiency = (actual_output/effective_capacity)
    return efficiency
#......................................................................................................................
def expected_output(effective_capacity:int,actual_output:int)->float:
    eff = efficiency(actual_output,effective_capacity)
    expected_output = effective_capacity * eff
    return expected_output
#......................................................................................................................
def break_even_in_units(total_fixed_cost:int,price:int,variable_cost:int)->float:
    denominatior = (price-variable_cost)
    break_even_in_units = (total_fixed_cost/denominatior)
    return break_even_in_units
#......................................................................................................................
def break_even_in_currency(total_fixed_cost:int,variable_cost,price:int)->float:
    denominator = (price-variable_cost)/price
    break_even_in_currency = (total_fixed_cost/denominator)
    return break_even_in_currency
#......................................................................................................................
def labour_cost_per_unit(labour_cost_per_day:int,total_production_per_day:int)-> float:
    labour_cost_per_unit = (labour_cost_per_day/total_production_per_day)
    return labour_cost_per_unit
#......................................................................................................................
def takt_time(total_available_worktime:int,units_required_to_satisfy_customer_demand:int)->float:
    takt_time = (total_available_worktime/units_required_to_satisfy_customer_demand)
    return takt_time
#......................................................................................................................
def workers_required(total_operational_time_required:int,takt_time:int)->float:
    workers_required = total_operational_time_required/takt_time
    return workers_required
#......................................................................................................................
def cycle_time(total_production_per_day:int,units_produced_per_day:int)->float:
    cycle_time = (total_production_per_day/units_produced_per_day)
    return cycle_time
#......................................................................................................................
def idle_time(number_of_work_station:int,largest_cycle_time:int,task_time:list)->float:
    total_task_time = 0 
    for time in task_time:
        total_task_time += time

    idle_time = (number_of_work_station*largest_cycle_time) - total_task_time

    return idle_time
#......................................................................................................................
def normal_time(average_observed_time:int,performance_rating_factor)->float:
    normal_time = average_observed_time*performance_rating_factor
    return normal_time
#......................................................................................................................
def standard_time(total_normal_time:float,allowance_factor:float)->float:
    standard_time = (total_normal_time/(1-allowance_factor))
    return standard_time
#......................................................................................................................
def inventory_turnover(cost_of_goods_sold:int,average_inventory_investment:float)->float:
    inventory_turnover = (cost_of_goods_sold/average_inventory_investment)
    return inventory_turnover
#......................................................................................................................
def weeks_of_supply(average_inventory_investment:float,annual_cost_of_goods_sold:float)->float:
    weeks_of_supply = average_inventory_investment/(annual_cost_of_goods_sold/52)
    return weeks_of_supply
#......................................................................................................................
def percentage_invested_in_inventory(total_assets:int,average_inventory_investment:float)->float:
    percentage_invested_in_inventory = (average_inventory_investment/total_assets)*100
    return percentage_invested_in_inventory

def bullwhip(variance_of_orders:float,variance_of_demand:float)->float:
    bullwhip = (variance_of_orders/variance_of_demand)
    return bullwhip
#......................................................................................................................
def annual_setup_cost(annual_demand_in_units:int,number_of_units_per_order:int,ordering_cost_per_order:float)->float:
    annual_setup_cost = (annual_demand_in_units/number_of_units_per_order)*ordering_cost_per_order
    return annual_setup_cost
#......................................................................................................................
def annual_holding_cost(average_inventory_level:float,holding_cost_per_unit:float)->float:
    annual_holding_cost = average_inventory_level*holding_cost_per_unit
    return annual_holding_cost
#......................................................................................................................
def optimal_order_quantity(holding_cost_per_unit:float,annual_demand_in_units:int,ordering_cost_per_order:float)->float:
    optimal_order_quantity = math.sqrt((2*annual_demand_in_units*ordering_cost_per_order)/holding_cost_per_unit)
    return optimal_order_quantity
#......................................................................................................................
def reorder_point(demand_per_day:int,lead_time_for_new_order_in_days:int,safety_stock:int=1)->int:
    reorder_point = (demand_per_day*lead_time_for_new_order_in_days)*safety_stock
    return reorder_point
#......................................................................................................................
def demand_per_day(annual_demand:float,total_working_days:int)->float:
    demand_per_day = (annual_demand/total_working_days)
    return demand_per_day
#......................................................................................................................
def service_level(sales_price_per_unit:float,cost_per_unit:float,salvage_value_per_unit:float= 0)->float:
    cost_of_shortage = sales_price_per_unit-cost_per_unit
    cost_of_overage = cost_per_unit-salvage_value_per_unit

    service_level = cost_of_shortage/(cost_of_shortage-cost_of_overage)
    return service_level
#......................................................................................................................
def critical_ratio(days_remaining_for_job:int,total_days_remaining:int)->float:
    critical_ratio = (days_remaining_for_job/total_days_remaining)
    return critical_ratio

#......................................................................................................................
















