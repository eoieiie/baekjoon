import sys

def main() -> None:
  read = sys.stdin.readline
  n = int(read())
  stock = [int(read()) for i in range(14)]
 
  def bnp() -> int:
    quantity = 0
    cash = n

    for price in stock:
        if cash >= price:
            buy = cash // price         
            quantity += buy
            cash -= buy * price         

    total_asset = cash + (quantity * stock[-1])
    return total_asset

  def tmng() -> int:
    increase = 0
    decrease = 0
    quantity = 0
    cash = n

    for i in range(1, len(stock)):
        if stock[i] > stock[i - 1]:
            increase += 1
            decrease = 0
        elif stock[i] < stock[i - 1]:
            decrease += 1
            increase = 0
        else:
            increase = 0
            decrease = 0

        # 연속상승전량매도
        if increase >= 3 and quantity > 0:
            cash += quantity * stock[i]
            quantity = 0

        # 연속하락전액매수
        elif decrease >= 3 and cash >= stock[i]:
            buy = cash // stock[i]
            quantity += buy
            cash -= buy * stock[i]

    total_asset = cash + (quantity * stock[-1])
    return total_asset
    
  bnp_result = bnp()#여러 번 호출하지 말고 변수에 저장해서 사용하면 빠름
  tmng_result = tmng()

  if bnp_result > tmng_result:
      print("BNP")
  elif bnp_result < tmng_result:
      print("TIMING")
  else:
      print("SAMESAME")
    
if __name__ == "__main__":
  main()
  