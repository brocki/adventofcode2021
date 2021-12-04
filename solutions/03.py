def evaluate(inputs: list) -> int:
  tmp = find_most_common(inputs)
  
  output = ""
  for char in tmp:
    if char > 0:
      output += "1"
    else:
      output += "0"

  bitmask = int("".ljust(len(tmp), "1"), 2)
  gamma = int(output, 2)
  epsilon = int(format(~gamma & bitmask, "0"+str(len(tmp))+"b"), 2)
  power = gamma * epsilon

  return {'gamma': gamma, 'gamma_bin': output, 'epsilon': epsilon, 'epsilon_bin': format(~gamma & 0b11111, "0"+str(len(tmp))+"b"), 'power': power}


def find_most_common(lines: list) -> list:
  tmp = []
  for char in lines[0]:
    tmp.append(0)
  
  for line in lines:
    for idx, char in enumerate(line):
      if char == "1":
        tmp[idx] += 1
      else:
        tmp[idx] += -1 
  return tmp


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