import random
import pandas as pd

class OTC(object):

    def __init__(self,id,hold_duration,call_time):
        self.id = id
        self.hold_duration = hold_duration
        self.call_time = call_time

    def __repr__(self):
        return "OTC attributes('{}', '{}', '{}')".format(self.id, self.hold_duration, self.call_time)


def supplier_objects(n):
    """
    This function will return a list of objects of the Suppliers with the OTC attributes id,hold duration and the call time
    :param n: number of suppliers in queue:
    :return: list of objects created
    """
    suppliers_list = []
    #random.seed(0)
    for i in range(n):
        id = i + 1
        call_time = int(random.randint(1, 12))
        hold_duration = int(random.randint(2,29))
        otc_object = OTC(id, hold_duration, call_time)
        otc_object.attr = n
        suppliers_list.append(otc_object)
    return suppliers_list

def employee_pop(emp, n, pop_count, suppliers_list):
    """
    1 st popup of callers depending on number of employees
    :param emp: number of employees available to attend supplier calls
    :param n: number of suppliers
    :param pop_count: count number of  popped elements from list
    :param suppliers_list: list of supplier objects
    :return: supplier list of objects, list e to find min wait time and updated count of normal popups
    """
    w = []
    if len(suppliers_list) == n:
        if emp == 1:
            w.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            pop_count += 1
        if emp == 2:
            w.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            pop_count += 1
            w.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            pop_count += 1
        if emp == 3:
            w.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            pop_count += 1
            w.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            pop_count += 1
            w.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            pop_count += 1
        if emp == 4:
            w.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            pop_count += 1
            w.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            pop_count += 1
            w.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            pop_count += 1
            w.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            pop_count += 1
    return suppliers_list, w, pop_count





def otc_performance_variables(emp, drop_count, w, n, pop_count, total_wait_time, drop_avg1, average_speed_answer1_1, drop_avg2, average_speed_answer2_2, drop_avg3, average_speed_answer3_3, drop_avg4, average_speed_answer4_4):
    """
    Function to calculate all the performance variables like drop rate and average speed of answer
    :param emp: number of employees
    :param drop_count: number of calls dropped
    :param w: list containing wait time depending on number of employees 
    :param n: number of suppliers
    :param pop_count: count number of pops from list
    :param total_wait_time: contains total wait time suppliers have to wait
    :param drop_avg1: addition of drop percentage in every iteration for employee = 1
    :param average_speed_answer1_1: addition of average speed of answer in every iteration for employee = 1
    :param drop_avg2: addition of drop percentage in every iteration for employee = 2
    :param average_speed_answer2_2: addition of average speed of answer in every iteration for employee = 2
    :param drop_avg3: addition of drop percentage in every iteration for employee = 3
    :param average_speed_answer3_3: addition of average speed of answer in every iteration for employee = 3
    :param drop_avg4: addition of drop percentage in every iteration for employee = 4
    :param average_speed_answer4_4: addition of average speed of answer in every iteration for employee = 4
    :return: addition of average speed of answer and drop percentage in every iteration for employee = 1,2,3,4
    """
    if emp == 1:
        drop1 = (drop_count / n) * 100
        drop_avg1 += drop1
        total_wait_time += min(w)
        average_speed_answer1 = total_wait_time / pop_count
        average_speed_answer1_1 += average_speed_answer1

    if emp == 2:
        drop2 = (drop_count / n) * 100
        drop_avg2 += drop2
        total_wait_time += min(w)
        average_speed_answer2 = total_wait_time / pop_count
        average_speed_answer2_2 += average_speed_answer2

    if emp == 3:
        drop3 = (drop_count / n) * 100
        drop_avg3 += drop3
        total_wait_time += min(w)
        average_speed_answer3 = total_wait_time / pop_count
        average_speed_answer3_3 += average_speed_answer3

    if emp == 4:
        drop4 = (drop_count / n) * 100
        drop_avg4 += drop4
        total_wait_time += min(w)
        average_speed_answer4 = total_wait_time / pop_count
        average_speed_answer4_4 += average_speed_answer4

    return drop_avg1, drop_avg2, drop_avg3, drop_avg4, average_speed_answer1_1, average_speed_answer2_2, average_speed_answer3_3,average_speed_answer4_4



def count_no_of_zeros(w, suppliers_list, cnt, pop_count, total_wait_time):
    """
    Count the number of zeroes in w and pop them as the supplier has attended the call and append the next suppliers call duration.
    :param w: list containing wait time depending on number of representatives
    :param suppliers_list: list of objects
    :param cnt: number of 0's found in list w
    :param pop_count: count number of normal pop from list 
    :param total_wait_time: contains total wait time suppliers have to wait
    :return:
    """
    if 0 in w:
        if len(suppliers_list) != 0:
            if cnt == 1:
                w.remove(0)
                w.append(suppliers_list[0].call_time)
                suppliers_list.remove(suppliers_list[0])
                pop_count += 1
            if cnt == 2:
                if len(suppliers_list) > 2:
                    w.remove(0);w.remove(0)
                    w.append(suppliers_list[0].call_time)
                    w.append(suppliers_list[1].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                elif len(suppliers_list) == 2:
                    w.remove(0);w.remove(0)
                    w.append(suppliers_list[0].call_time)
                    w.append(suppliers_list[1].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    total_wait_time += min(w)
                elif len(suppliers_list) == 1:
                    w.remove(0)
                    w.append(suppliers_list[0].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    total_wait_time+=min(w)

            if cnt == 3:
                if len(suppliers_list) > 3:
                    w.remove(0);w.remove(0);w.remove(0)
                    w.append(suppliers_list[0].call_time)
                    w.append(suppliers_list[1].call_time)
                    w.append(suppliers_list[2].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                elif len(suppliers_list) == 3:
                    w.remove(0);w.remove(0);w.remove(0)
                    w.append(suppliers_list[0].call_time)
                    w.append(suppliers_list[1].call_time)
                    w.append(suppliers_list[2].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    total_wait_time += min(w)
                elif len(suppliers_list) == 2:
                    w.remove(0);w.remove(0)
                    w.append(suppliers_list[0].call_time)
                    w.append(suppliers_list[1].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    total_wait_time += min(w)
                elif len(suppliers_list) == 1:
                    w.remove(0)
                    w.append(suppliers_list[0].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    total_wait_time += min(w)
            if cnt == 4:
                if len(suppliers_list) > 4:
                    w.remove(0);w.remove(0);w.remove(0);w.remove(0)
                    w.append(suppliers_list[0].call_time)
                    w.append(suppliers_list[1].call_time)
                    w.append(suppliers_list[2].call_time)
                    w.append(suppliers_list[3].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                elif len(suppliers_list) == 4:
                    w.remove(0);w.remove(0);w.remove(0);w.remove(0)
                    w.append(suppliers_list[0].call_time)
                    w.append(suppliers_list[1].call_time)
                    w.append(suppliers_list[2].call_time)
                    w.append(suppliers_list[3].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    total_wait_time += min(w)
                elif len(suppliers_list) == 3:
                    w.remove(0);w.remove(0);w.remove(0)
                    w.append(suppliers_list[0].call_time)
                    w.append(suppliers_list[1].call_time)
                    w.append(suppliers_list[2].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    total_wait_time += min(w)
                elif len(suppliers_list) == 2:
                    w.remove(0);w.remove(0)
                    w.append(suppliers_list[0].call_time)
                    w.append(suppliers_list[1].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    total_wait_time += min(w)
                elif len(suppliers_list) == 1:
                    w.remove(0)
                    w.append(suppliers_list[0].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    pop_count += 1
                    total_wait_time += min(w)
        elif len(suppliers_list) == 0:
            total_wait_time += min(w)

    return pop_count, total_wait_time, suppliers_list , w

def otc_performance_variables_2000_simulation(emp, dropratelist, asalist, drop_avg1, drop_avg2, drop_avg3, drop_avg4, average_speed_answer1_1, average_speed_answer2_2, average_speed_answer3_3,average_speed_answer4_4):
    """
    Program to calculate otc performance variables of drop rate and average speed of answer for 2000 simulations
    :param emp:
    :param dropratelist: list containing average drop rate for employees 1,2,3,4 for 2000 simulations
    :param asalist: list containing average speed of answer for employees 1,2,3,4 for 2000 simulations
    :param drop_avg1: addition of drop percentage in every iteration for employee = 1
    :param drop_avg2: addition of drop percentage in every iteration for employee = 2
    :param drop_avg3: addition of drop percentage in every iteration for employee = 3
    :param drop_avg3: addition of drop percentage in every iteration for employee = 4
    :param average_speed_answer1_1: addition of average speed of answer in every iteration for employee = 1
    :param average_speed_answer2_2: addition of average speed of answer in every iteration for employee = 2
    :param average_speed_answer3_3: addition of average speed of answer in every iteration for employee = 3
    :param average_speed_answer4_4: addition of average speed of answer in every iteration for employee = 4
    :return: dropratelist, asalist
    """
    if emp == 1:
        dropratelist.append(drop_avg1 / 2000)
        asalist.append(average_speed_answer1_1 / 2000)
    elif emp == 2:
        dropratelist.append(drop_avg2 / 2000)
        asalist.append(average_speed_answer2_2 / 2000)
    elif emp == 3:
        dropratelist.append(drop_avg3 / 2000)
        asalist.append(average_speed_answer3_3 / 2000)
    elif emp == 4:
        dropratelist.append(drop_avg4 / 2000)
        asalist.append(average_speed_answer4_4 / 2000)

    return dropratelist, asalist

def drop_calls(wait_time, drop_count, supplier_list, w):
    """
    Function works as a counter to check if wait time is over
    :param wait_time: wait time callers have to wait 
    :param drop_count: number of calls dropped
    :param supplier_list: list of objects
    :param w: list containing wait time depending on number of employees
    :param count: timer count
    :return: wait time, number of calls dropped, list of objects, list w, and timer count
    """
    for member in supplier_list:
        if member.hold_duration <= wait_time:
            drop_count += 1
            supplier_list.remove(member)

    for member in supplier_list:
        member.hold_duration = member.hold_duration - wait_time
        if member.hold_duration <= 0:
            drop_count += 1
            supplier_list.remove(member)
    w = [x - wait_time for x in w]


    return wait_time, drop_count, supplier_list, w


if __name__ == '__main__':
    random.seed(0)
    dropratelist = []
    asalist = []
    suppliers_list = []
    total_wait_time = 0
    for emp in range(1, 5): #Loop for Employees 1,2,3,4
        drop_avg1 = 0
        drop_avg2 = 0
        drop_avg3 = 0
        drop_avg4 = 0
        average_speed_answer1_1 = 0
        average_speed_answer2_2 = 0
        average_speed_answer3_3 = 0
        average_speed_answer4_4 = 0
        for k in range(2000):   # loop for 2000 simulations
            suppliers_list = []
            w = []
            drop_count = 0
            pop_count = 0
            n = int(random.randint(10,20))
            suppliers_list = supplier_objects(n)
            suppliers_list, w, pop_count = employee_pop(emp, n, pop_count, suppliers_list)

            drop1 = 0
            drop2 = 0
            drop3 = 0
            drop4 = 0
            average_speed_answer1 = 0
            average_speed_answer2 = 0
            average_speed_answer3 = 0
            average_speed_answer4 = 0
            total_wait_time = 0

            for i in range(len(suppliers_list)):
                if len(suppliers_list) != 0:
                    wait_time = min(w)
                    total_wait_time = total_wait_time + wait_time
                    wait_time, drop_count, d, e = drop_calls(wait_time, drop_count, suppliers_list, w)
                    cnt = w.count(0)
                    pop_count, total_wait_time, suppliers_list, w = count_no_of_zeros(w, suppliers_list, cnt, pop_count,total_wait_time)

            drop_avg1, drop_avg2, drop_avg3,drop_avg4, average_speed_answer1_1, average_speed_answer2_2, average_speed_answer3_3,average_speed_answer4_4 = otc_performance_variables(emp, drop_count, w, n, pop_count,  total_wait_time, drop_avg1, average_speed_answer1_1, drop_avg2, average_speed_answer2_2, drop_avg3, average_speed_answer3_3, drop_avg4, average_speed_answer4_4)

        dropratelist, asalist = otc_performance_variables_2000_simulation(emp, dropratelist, asalist, drop_avg1, drop_avg2, drop_avg3, drop_avg4, average_speed_answer1_1, average_speed_answer2_2, average_speed_answer3_3,average_speed_answer4_4)

    employee_list = [1, 2, 3, 4]

    print("Monte Carlo Simulation for Over The Counter Trading")
    print("\nHypothesis - True: As number of employees increase Dropout Percentage and Avg wait time decrease")
    print("The lower your Avg Response time, the shorter amount of time that the suppliers are waiting in the queue.")

    print("\nNumber of Employees and the Avg dropout percentage")
    dropout_matrix=pd.DataFrame(list(dict(zip(employee_list,dropratelist)).items()), columns=['Number Of Employees', 'Dropout Percentage'])
    dropout_matrix.set_index('Number Of Employees',inplace=True)
    print(dropout_matrix)


    print("\nNumber of Employees and the Response Time ")
    asa_matrix=pd.DataFrame(list(dict(zip(employee_list,asalist)).items()), columns=['Number Of Employees', 'Average Response Time'])
    asa_matrix.set_index('Number Of Employees',inplace=True)
    print(asa_matrix)






