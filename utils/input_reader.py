import os

def load_file(filename, row_delimeter, col_delimeter):
    if row_delimeter is None and col_delimeter is not None:
        raise Exception("Must specify row delimeter to use col delimeter")
    
    out = None
    
    with open(filename, "r") as f:
        out = f.read()

    if row_delimeter is not None:
        out = out.split(row_delimeter)

        if col_delimeter is not None:
            out = [row.split(col_delimeter) for row in out]
    
    return out

def load(file_path, sample_file_name, input_file_name, row_delimeter, col_delimeter):
    dir_name = os.path.split(file_path)[1].rstrip(".py")

    sample_input_path = os.path.join(dir_name, sample_file_name)
    input_path = os.path.join(dir_name, input_file_name)

    sample_data = load_file(sample_input_path, row_delimeter, col_delimeter)
    data = load_file(input_path, row_delimeter, col_delimeter)

    return sample_data, data