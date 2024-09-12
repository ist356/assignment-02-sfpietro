'''
This is a module for parsing packging data
'''

def parse_packaging(packaging_data: str) -> list[dict]:
    '''
    This function parses a string of packaging data and returns a list of dictionaries.
    The order of the list implies the order of the packaging data.

    Examples:

    input: "12 eggs in 1 carton" 
    ouput: [{ 'eggs' : 12}, {'carton' : 1}]

    input: "6 bars in 1 pack / 12 packs in 1 carton"
    output: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]

    input: "20 pieces in 1 pack / 10 packs in 1 carton / 4 cartons in 1 box"
    output: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    '''
    item_list = packaging_data.split(" / ")
    package_list = []
    for item in item_list:
        item_split = item.split(" in ")
        for item in item_split:
            packaging = item.split()
            package_dict = {packaging[0]:packaging[1]}
            package_list.append(package_dict) ## need to fix this so the output matches the above will proabbly aslo have to fix the text belows
    return package_list


def calc_total_units(package: list[dict]) -> int:
    '''
    This function calculates the total number of items in a package

    Example:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output 72 (e.g. 6*12*1)

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: 800 (e.g. 20*10*4*1)
    '''
    total = 1
    for dict in package:
        for key in dict.items():
            key_num = int(key[0])
            total = total * key_num
    return total


def get_unit(package: list[dict]) -> str:
    '''
    This function returns the items in the packaging (this is the first item in the list)

    Examples:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output: bars

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: pieces

    '''
    unit_dict = package[0]
    for unit in unit_dict:
        key = unit_dict[unit]
    return(key)




# This will only run from here, not when imported
# # Use this for testing / debugging cases with the debugger
if __name__ == '__main__':
    
    text = "6 bars in 1 pack / 12 packs in 1 carton"
    package = parse_packaging(text)
    print(package)

    package_total = calc_total_units(package)
    unit = get_unit(package)
    print(f"{package_total} {unit} total")