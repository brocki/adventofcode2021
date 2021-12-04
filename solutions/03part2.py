def evaluate(inputs: list) -> int:
  oxygen = find_gas_indicator("MOST", 0, inputs)[0]
  co2 = find_gas_indicator("LEAST", 0, inputs)[0]

  return {'oxygen': int(oxygen, 2), 'oxygen_bin': oxygen, 'co2': int(co2, 2), 'co2_bin': co2, 'life_support': int(oxygen, 2) * int(co2, 2)}


def find_common(type: str, position, lines: list) -> int:
  cnt = 0
  for line in lines:
    if line[position] == "1":
      cnt += 1
    else:
      cnt += -1

  if cnt < 0:
    output = 0
  else:
    output = 1 
  if type == "MOST":
    return output
  else:
    return int(not output)


def filter_inputs(condition: int, position: int, inputs: list) -> list:
  filtered_list = []
  for input in inputs:
    if input[position] == str(condition):
      filtered_list.append(input)
  return filtered_list


def find_gas_indicator(search_type: str, position: int, inputs: list) -> list:
  crit = find_common(search_type, position, inputs) 
  data = filter_inputs(crit, position, inputs)
  if len(data) == 1:
    return data
  else:
    crit = find_common(search_type, position+1, data)
    return find_gas_indicator(search_type, position+1, data)


def main():
  inputs = []
  while True:
      try:
        input_ = input("")
        if input_ == "":
          break
        inputs.append(input_)
      except EOFError:
          break
  print(evaluate(inputs))


if __name__ == '__main__':
  main()