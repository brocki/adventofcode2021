def evaluate(data: list) -> int:
  last = None
  cnt = 0
  for entry in data:
    if last and entry > last:
      cnt += 1
    last = entry
  return cnt

def main():
  data = []
  while True:
      try:
        input_ = input("")
        if input_ == "":
          break
        data.append(int(input_))
      except EOFError:
          break
  print(evaluate(data))

if __name__ == '__main__':
  main()