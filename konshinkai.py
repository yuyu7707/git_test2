times = int(input("何杯目ですか？: "))

drinks = ["ビール", "ビール", "ビール", "レモンサワー", "レモンサワー"]

times_to_key = times - 1
final_drink = len(drinks)-1

if times_to_key < 0 or times_to_key > final_drink:
    print("範囲外です")
elif times_to_key == 0:
    print(drinks[times_to_key])
    print("乾杯")
elif times_to_key == final_drink:
    print(drinks[final_drink])
    print("お疲れ様でした")
else:
    print(drinks[times_to_key])
    print("楽しいなー")
