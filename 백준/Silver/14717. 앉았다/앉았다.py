import sys

def main() -> None:
    read = sys.stdin.readline

    def strength(a, b):
        if a == b:  # 땡
            return 100 + a  # 처음부터 겁나 크게
        else:  # 끗
            return (a + b) % 10  # 0부터 시작
    # 카드 20개
    cards = [i for i in range(1, 11) for _ in range(2)]

    # 패 입력
    card_a, card_b = map(int, read().split())

    # 뽑은 카드 제거
    cards.remove(card_a)
    cards.remove(card_b)

    # 영학쓰 족보 강도
    yh_strength = strength(card_a, card_b)

    # 남은 18장에서 2장을 뽑는 모든 조합
    win_count = 0
    total_count = 0

    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            opponent_strength = strength(cards[i], cards[j])
            total_count += 1

            if yh_strength > opponent_strength:
                win_count += 1
              
    prob = win_count / total_count

    sys.stdout.write(f"{prob:.3f}\n")

if __name__ == "__main__":
    main()