from exception import logging
import logger_file

def get_data_from_bd(file_data: str) -> list[list[str]]:
    try:
        file_data = file_data.replace('-', '')
        file_data = file_data.replace(' ', '')
        file_data = file_data.replace('\n', ' ')
        lst = []
        if '  ' in file_data:
            file_data = file_data.split('  ')
            for word in file_data:
                if word != '':
                    s = word.split(' ')
                    lst.append(s)
            return lst
        elif ';' in file_data:
            file_data = file_data.split(' ')
            for word in file_data:
                if word != '':
                    s = word.split(';')
                    lst.append(s)
            return lst
            logger_file.log_info(f'Requested a record: {lst}', 'get_data_from_bd')
    except Exception as e:
        logging.debug(e)


def search_by_input_info(input_info: str, input_array: list[list[str]]) -> list[list[str]]:
    try:
        output = []
        for hi_level_item in input_array:
            for low_level_item in hi_level_item:
                if input_info in low_level_item:
                    output.append(hi_level_item)
        return output
        logger_file.log_info(f'Searched a record: {output}', 'get_data_from_bd')
    except Exception as e:
        logging.debug(e)


def add_new_line_in_bd(input_method):
    return input_method
    logger_file.log_info(f'Searched a record: {input_method}', 'add_new_line_in_bd')


def delete_much_contact(input_matching_line: list, input_array: list[list[str]]) -> list[list[str]]:
    try:
        output_array = []
        for hi_level_item in input_array:
            if input_matching_line != hi_level_item:
                output_array.append(hi_level_item)

        return output_array
        logger_file.log_info(f'Searched a record: {output_array}', 'delete_much_contact')
    except Exception as e:
        logging.debug(e)
