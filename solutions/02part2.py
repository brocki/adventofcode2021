def evaluate(inputs: list) -> int:
  hor = 0
  depth = 0
  aim = 0
  for line in inputs:
    direction, distance = line.split(" ")
    if direction == "forward":
      hor += int(distance)
      depth += aim * int(distance)
    elif direction == "up":
      aim += -int(distance)
    elif direction == "down":
      aim += int(distance)
  return {"horiz": hor, "depth": depth, "multiply": hor * depth}


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