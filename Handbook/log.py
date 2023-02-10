import datetime

log_filename = './log.txt'


def add_log_record(record: str):

    with open(log_filename, 'a', encoding='utf-8') as logfile:
        logfile.write(f'{datetime.datetime.now()}: {record}\n')
