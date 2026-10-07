def create_time_checker(max_time):
    def time_checker(time):
        if time > max_time:
            return 'Лимит превышен'
        else:
            return 'Лимит не превышен'

    return time_checker


time_checker_4 = create_time_checker(4)
time_checker_3 = create_time_checker(3)
print(time_checker_4(3))
print(time_checker_3(4))
