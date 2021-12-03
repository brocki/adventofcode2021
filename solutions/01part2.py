def evaluate(data: list) -> int:
  last = None
  cnt = 0
  for idx, entry in enumerate(data):
    tmp_l = data[idx:idx+3]
    if len(tmp_l) < 3:
      break
    s = sum(tmp_l)
    if last and s > last:
      cnt += 1
    last = s
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