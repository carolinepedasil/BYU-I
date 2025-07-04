def process_hr_data(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split(' ')
            name = parts[0]
            id_number = parts[1]
            job_title = parts[2]
            salary = float(parts[3])

            paycheck_amount = (salary / 12) * 2

            if job_title == "Engineer":
                paycheck_amount += 1000

            print(f"{name} (ID: {id_number}), {job_title} - ${paycheck_amount:.2f}")

process_hr_data('/Users/caroline/BYU-I/CSEPC 110 - Introduction to Programming/Team Activity/hr_system.txt')
