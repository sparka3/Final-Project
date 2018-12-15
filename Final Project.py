import random
import pandas as pd
import doctest

class OTC(object):
    """
    Object to store supplier call details
    """
    def __init__(self,id,hold_duration,call_time):
        self.id = id
        self.hold_duration = hold_duration
        self.call_time = call_time

    def __repr__(self):
        return "OTC attributes('{}', '{}', '{}')".format(self.id, self.hold_duration, self.call_time)

def supplier_queue(n):
    """
    The supplier_queue function will return a list of objects of the Suppliers with the following attributes : Call Id,Hold Duration, Call Time
    :param n: number of suppliers in queue:
    :return: list of objects created
    >>> test = supplier_queue(10)
    >>> print(test)
    [OTC attributes('1', '15', '7'), OTC attributes('2', '10', '1'), OTC attributes('3', '17', '9'), OTC attributes('4', '11', '7'), OTC attributes('5', '13', '8'), OTC attributes('6', '8', '10'), OTC attributes('7', '6', '9'), OTC attributes('8', '6', '5'), OTC attributes('9', '10', '2'), OTC attributes('10', '6', '9')]
    """
    random.seed(0)
    suppliers_list = []
    for i in range(n):
        id = i + 1
        call_time = int(random.randint(1, 12)) # The values 1 and  12 have been considered because the call time of a supplier will be for minimum 1 minute and maximum 12 minutes
        hold_duration = int(random.randint(2,20)) # The values 2 and  20 have been considered because the call wait time of a supplier will be for minimum 2 minutes and maximum 29 minutes
        otc_object = OTC(id, hold_duration, call_time)
        otc_object.attr = n
        suppliers_list.append(otc_object)
    return suppliers_list

def employee_pop(emp, n, call_attended, suppliers_list):
    """  The employee_pop function will pop callers depending on number of employees and the number of suppliers
    :param emp: number of employees available to attend the calls of suppliers
    :param n:  number of suppliers calling
    :param call_attended: count number of removed elements from list i.e. the
    :param suppliers_list: list of supplier objects containing details of id, hold_duration and call_time
    :return: function returns supplier list of objects, list of min_call_duration that displays min wait time and call_attended updated count
    >>> test = supplier_queue(10)
    >>> test2 = employee_pop(1, 10, 0, test)
    >>> print(test2)
    ([OTC attributes('2', '10', '1'), OTC attributes('3', '17', '9'), OTC attributes('4', '11', '7'), OTC attributes('5', '13', '8'), OTC attributes('6', '8', '10'), OTC attributes('7', '6', '9'), OTC attributes('8', '6', '5'), OTC attributes('9', '10', '2'), OTC attributes('10', '6', '9')], [7], 1)
    """
    min_call_duration = []
    if len(suppliers_list) == n:
    # If the number of employees are 1, the employee will attend the 1st supplier and the supplier will be removed from the suppliers list
        if emp == 1:
            min_call_duration.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            call_attended += 1
    # If the number of employees are 2, the respective employees will attend one supplier call individually and the supplier details  will
    # be removed from the suppliers list
        if emp == 2:
            min_call_duration.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            call_attended += 1
            min_call_duration.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            call_attended += 1
    # If the number of employees are 3, the respective employees will attend one supplier call individually and the supplier details  will
    # be removed from the suppliers list
        if emp == 3:
            min_call_duration.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            call_attended += 1
            min_call_duration.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            call_attended += 1
            min_call_duration.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            call_attended += 1
    # If the number of employees are 4, the respective employees will attend one supplier call individually and the supplier details  will
    # be removed from the suppliers list
        if emp == 4:
            min_call_duration.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            call_attended += 1
            min_call_duration.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            call_attended += 1
            min_call_duration.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            call_attended += 1
            min_call_duration.append(suppliers_list[0].call_time)
            suppliers_list.pop(0)
            call_attended += 1
    return suppliers_list, min_call_duration, call_attended

def otc_performance_variables(emp, drop_count, min_call_duration, n, call_attended, total_wait_time,average_drop1, avg_response_time1_1, average_drop2, avg_response_time2_2, average_drop3, avg_response_time3_3, average_drop4, avg_response_time4_4):
    """ The otc_performance_variables function calculates the drop rate of calls and the average speed of answer by the employee
    :param emp: number of employees
    :param drop_count: number of  supplier calls dropped
    :param min_call_duration: wait time based on number of employees
    :param n: number of suppliers
    :param call_attended: number of calls attended, i.e. the number of calls removed from the list
    :param total_wait_time: total wait time suppliers have to wait before being attended
    :param average_drop1: For employee = 1, average_drop1 adds the drop percentage with every iteration
    :param avg_response_time1_1: For employee = 1, avg_response_time1_1 adds the average response time with every iteration
    :param average_drop2: For employee = 2, average_drop1 adds the drop percentage with every iteration
    :param avg_response_time2_2: For employee = 2, avg_response_time1_1 adds the average response time with every iteration
    :param average_drop3: For employee = 3, average_drop1 adds the drop percentage with every iteration
    :param avg_response_time3_3: For employee = 3, avg_response_time1_1 adds the average response time with every iteration
    :param average_drop4: For employee = 4, average_drop1 adds the drop percentage with every iteration
    :param avg_response_time4_4: For employee = 4, avg_response_time1_1 adds the average response time with every iteration
    :return: For the 1,2,3,4 employees, the function returns the addition of average response time with each iteration
    >>> test3=otc_performance_variables(1,15,[7],16,1,42,0,0,0,0,0,0,0,0)
    >>> print(test3)
    (93.75, 0, 0, 0, 49.0, 0, 0, 0)
    """
    if emp == 1:
        drop1 = (drop_count / n) * 100
        average_drop1 += drop1
        total_wait_time += min(min_call_duration)
        avg_response_time1 = total_wait_time / call_attended
        avg_response_time1_1 += avg_response_time1

    if emp == 2:
        drop2 = (drop_count / n) * 100
        average_drop2 += drop2
        total_wait_time += min(min_call_duration)
        avg_response_time2 = total_wait_time / call_attended
        avg_response_time2_2 += avg_response_time2

    if emp == 3:
        drop3 = (drop_count / n) * 100
        average_drop3 += drop3
        total_wait_time += min(min_call_duration)
        avg_response_time3 = total_wait_time / call_attended
        avg_response_time3_3 += avg_response_time3

    if emp == 4:
        drop4 = (drop_count / n) * 100
        average_drop4 += drop4
        total_wait_time += min(min_call_duration)
        avg_response_time4 = total_wait_time / call_attended
        avg_response_time4_4 += avg_response_time4
    return average_drop1, average_drop2, average_drop3, average_drop4, avg_response_time1_1, avg_response_time2_2, avg_response_time3_3,avg_response_time4_4

def zero_count(min_call_duration, suppliers_list, cnt, call_attended, total_wait_time):
    """
    The zero_count function counts the number of zeroes in the min_call_duration and pop them as the supplier has attended the call and append the next suppliers call duration.
    :param w: wait time depending on the number of representatives
    :param suppliers_list:
    :param cnt: number of 0's found in the list of min_call_duration
    :param call_attended: count of calls attended from list
    :param total_wait_time: contains total wait time of suppliers
    :return:
    >>> test = supplier_queue(16)
    >>> test4 = zero_count([7],test,0,1,7)
    >>> print(test4)
    (1, 7, [OTC attributes('1', '15', '7'), OTC attributes('2', '10', '1'), OTC attributes('3', '17', '9'), OTC attributes('4', '11', '7'), OTC attributes('5', '13', '8'), OTC attributes('6', '8', '10'), OTC attributes('7', '6', '9'), OTC attributes('8', '6', '5'), OTC attributes('9', '10', '2'), OTC attributes('10', '6', '9'), OTC attributes('11', '5', '5'), OTC attributes('12', '4', '12'), OTC attributes('13', '12', '11'), OTC attributes('14', '19', '8'), OTC attributes('15', '13', '2'), OTC attributes('16', '12', '7')], [7])
    """
    if 0 in min_call_duration:
        if len(suppliers_list) != 0:
            if cnt == 1:
                min_call_duration.remove(0)
                min_call_duration.append(suppliers_list[0].call_time)
                suppliers_list.remove(suppliers_list[0])
                call_attended += 1
            if cnt == 2:
                if len(suppliers_list) > 2:
                    min_call_duration.remove(0);min_call_duration.remove(0)
                    min_call_duration.append(suppliers_list[0].call_time)
                    min_call_duration.append(suppliers_list[1].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                elif len(suppliers_list) == 2:
                    min_call_duration.remove(0);min_call_duration.remove(0)
                    min_call_duration.append(suppliers_list[0].call_time)
                    min_call_duration.append(suppliers_list[1].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    total_wait_time += min(min_call_duration)
                elif len(suppliers_list) == 1:
                    min_call_duration.remove(0)
                    min_call_duration.append(suppliers_list[0].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    total_wait_time+=min(min_call_duration)

            if cnt == 3:
                if len(suppliers_list) > 3:
                    min_call_duration.remove(0);min_call_duration.remove(0);min_call_duration.remove(0)
                    min_call_duration.append(suppliers_list[0].call_time)
                    min_call_duration.append(suppliers_list[1].call_time)
                    min_call_duration.append(suppliers_list[2].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                elif len(suppliers_list) == 3:
                    min_call_duration.remove(0);min_call_duration.remove(0);min_call_duration.remove(0)
                    min_call_duration.append(suppliers_list[0].call_time)
                    min_call_duration.append(suppliers_list[1].call_time)
                    min_call_duration.append(suppliers_list[2].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    total_wait_time += min(min_call_duration)
                elif len(suppliers_list) == 2:
                    min_call_duration.remove(0);min_call_duration.remove(0)
                    min_call_duration.append(suppliers_list[0].call_time)
                    min_call_duration.append(suppliers_list[1].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    total_wait_time += min(min_call_duration)
                elif len(suppliers_list) == 1:
                    min_call_duration.remove(0)
                    min_call_duration.append(suppliers_list[0].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    total_wait_time += min(min_call_duration)
            if cnt == 4:
                if len(suppliers_list) > 4:
                    min_call_duration.remove(0);min_call_duration.remove(0);min_call_duration.remove(0);min_call_duration.remove(0)
                    min_call_duration.append(suppliers_list[0].call_time)
                    min_call_duration.append(suppliers_list[1].call_time)
                    min_call_duration.append(suppliers_list[2].call_time)
                    min_call_duration.append(suppliers_list[3].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                elif len(suppliers_list) == 4:
                    min_call_duration.remove(0);min_call_duration.remove(0);min_call_duration.remove(0);min_call_duration.remove(0)
                    min_call_duration.append(suppliers_list[0].call_time)
                    min_call_duration.append(suppliers_list[1].call_time)
                    min_call_duration.append(suppliers_list[2].call_time)
                    min_call_duration.append(suppliers_list[3].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    total_wait_time += min(min_call_duration)
                elif len(suppliers_list) == 3:
                    min_call_duration.remove(0);min_call_duration.remove(0);min_call_duration.remove(0)
                    min_call_duration.append(suppliers_list[0].call_time)
                    min_call_duration.append(suppliers_list[1].call_time)
                    min_call_duration.append(suppliers_list[2].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    total_wait_time += min(min_call_duration)
                elif len(suppliers_list) == 2:
                    min_call_duration.remove(0);min_call_duration.remove(0)
                    min_call_duration.append(suppliers_list[0].call_time)
                    min_call_duration.append(suppliers_list[1].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    total_wait_time += min(min_call_duration)
                elif len(suppliers_list) == 1:
                    min_call_duration.remove(0)
                    min_call_duration.append(suppliers_list[0].call_time)
                    suppliers_list.remove(suppliers_list[0])
                    call_attended += 1
                    total_wait_time += min(min_call_duration)
        elif len(suppliers_list) == 0:
            total_wait_time += min(min_call_duration)
    return call_attended, total_wait_time, suppliers_list , min_call_duration

def otc_performance_variables_overall_stats(emp, dropratelist, asalist, average_drop1, average_drop2, average_drop3, average_drop4, avg_response_time1_1, avg_response_time2_2, avg_response_time3_3,avg_response_time4_4):
    """
    The otc_performance_variable_overall_stats function calculates otc the drop rate and average speed of answer for 2000 simulations
    :param emp: employee
    :param dropratelist: average drop rate for 1,2,3,4 employees for 2000 simulations
    :param asalist: 1,2,3,4 employee average speed of answer list for 2000 simulations
    :param average_drop1: When employee = 1 for every iteration, there is addition of drop percentage
    :param average_drop2: When employee = 2 for every iteration, there is addition of drop percentage
    :param average_drop3: When employee = 3 for every iteration, there is addition of drop percentage
    :param average_drop3: When employee = 4 for every iteration, there is addition of drop percentage
    :param avg_response_time1_1: When employee = 1 for every iteration, there is addition of average response time
    :param avg_response_time2_2: When employee = 1 for every iteration, there is addition of average response time
    :param avg_response_time3_3: When employee = 1 for every iteration, there is addition of average response time
    :param avg_response_time4_4: When employee = 1 for every iteration, there is addition of average response time
    :return: dropratelist, asalist
    >>> test5 = otc_performance_variables_overall_stats(1,[],[],189468.25042217335,0,0,0,97986.0,0,0,0)
    >>> print(test5)
    ([94.73412521108668], [48.993])
    """
    if emp == 1:
        dropratelist.append(average_drop1 / 2000)
        asalist.append(avg_response_time1_1 / 2000)
    elif emp == 2:
        dropratelist.append(average_drop2 / 2000)
        asalist.append(avg_response_time2_2 / 2000)
    elif emp == 3:
        dropratelist.append(average_drop3 / 2000)
        asalist.append(avg_response_time3_3 / 2000)
    elif emp == 4:
        dropratelist.append(average_drop4 / 2000)
        asalist.append(avg_response_time4_4 / 2000)
    return dropratelist, asalist

def drop_calls(wait_time, drop_count, supplier_list, min_call_duration):
    """
    The drop calls function is a counter that checks the duration of the wait time if it is over
    :param wait_time: supplier wait time
    :param drop_count: count of calls dropped
    :param supplier_list: list of supplier objects
    :param min_call_duration: wait time depending on the number of employees
    :param count: timer
    :return: returns the wait time, the number of calls dropped, the list of suppliers, the list of min_call_duration, and timer
    >>> test = supplier_queue(13)
    >>> test6 = drop_calls(7,3,test,[7])
    >>> print(test6)
    (7, 8, [OTC attributes('1', '8', '7'), OTC attributes('2', '3', '1'), OTC attributes('3', '10', '9'), OTC attributes('4', '4', '7'), OTC attributes('5', '6', '8'), OTC attributes('6', '1', '10'), OTC attributes('9', '10', '2'), OTC attributes('13', '12', '11')], [0])
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
    min_call_duration = [x - wait_time for x in min_call_duration]
    return wait_time, drop_count, supplier_list, min_call_duration

if __name__ == '__main__':
    doctest.testmod()
    random.seed(0)
    dropratelist = []
    asalist = []
    suppliers_list = []
    total_wait_time = 0
    for emp in range(1, 5):
        average_drop1 = 0
        average_drop2 = 0
        average_drop3 = 0
        average_drop4 = 0
        avg_response_time1_1 = 0
        avg_response_time2_2 = 0
        avg_response_time3_3 = 0
        avg_response_time4_4 = 0
        for k in range(2000):
            suppliers_list = []
            min_call_duration = []
            drop_count = 0
            call_attended = 0
            n = int(random.randint(10,20))
            suppliers_list = supplier_queue(n)
            suppliers_list, min_call_duration, call_attended = employee_pop(emp, n, call_attended, suppliers_list)

            drop1 = 0
            drop2 = 0
            drop3 = 0
            drop4 = 0
            avg_response_time1 = 0
            avg_response_time2 = 0
            avg_response_time3 = 0
            avg_response_time4 = 0
            total_wait_time = 0

            for i in range(len(suppliers_list)):
                if len(suppliers_list) != 0:
                    wait_time = min(min_call_duration)
                    total_wait_time = total_wait_time + wait_time
                    wait_time, drop_count, d, e = drop_calls(wait_time, drop_count, suppliers_list, min_call_duration)
                    cnt = min_call_duration.count(0)
                    call_attended, total_wait_time, suppliers_list, min_call_duration = zero_count(min_call_duration, suppliers_list, cnt, call_attended,total_wait_time)

            average_drop1, average_drop2, average_drop3,average_drop4, avg_response_time1_1, avg_response_time2_2, avg_response_time3_3,avg_response_time4_4 = otc_performance_variables(emp, drop_count, min_call_duration, n, call_attended,  total_wait_time, average_drop1, avg_response_time1_1, average_drop2, avg_response_time2_2, average_drop3, avg_response_time3_3, average_drop4, avg_response_time4_4)

        dropratelist, asalist = otc_performance_variables_overall_stats(emp, dropratelist, asalist, average_drop1, average_drop2, average_drop3, average_drop4, avg_response_time1_1, avg_response_time2_2, avg_response_time3_3,avg_response_time4_4)

    employee_list = [1, 2, 3, 4]

    print("Monte Carlo Simulation for Over The Counter Trading")
    print("\nHypothesis - True: As number of employees increase Dropout Percentage and Avg wait time decrease")
    print("The lower your Avg Response time, the shorter amount of time that the suppliers are waiting in the queue.")

    matrix = {
        'No. of Employees': employee_list,
        'Dropout Percent': dropratelist,
        'Avg Response Time': asalist
    }
    table = pd.DataFrame(matrix).set_index('No. of Employees')
    print(table)