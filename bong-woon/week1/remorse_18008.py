# 모스 부호를 딕셔너리 객체에 저장
morse = {
    'A' : '.-', 'B' : '-...', 'C' : '-.-.', 'D' : '-..', 'E' : '.', 'F' : '..-.', 'G' : '--.', 'H' : '....', 'I' : '..',
    'J' : '.---', 'K' : '-.-', 'L' : '.-..', 'M' : '--', 'N' : '-.', 'O' : '---', 'P' : '.--.', 'Q' : '--.-', 'R' : '.-.',
    'S' : '...', 'T' : '-', 'U' : '..-', 'V' : '...-', 'W' : '.--', 'X' : '-..-', 'Y' : '-.--', 'Z' : '--..'
}

# 입력
s = input()

# 공백 및 특수문자 제거
s = s.replace(' ', '')
s = s.replace(',', '')
s = s.replace('.', '')
s = s.replace('"', '')
s = s.replace("'", '')

# 대소문자 구분이 없으므로 모두 대문자로 변환
s = s.upper()
print(s)

# 모스 부호의 길이 값 초기화
length = 0

# 입력된 문장의 알파벳을 하나씩 확인
for key in s:
    # 알파벳에 해당하는 모스 부호를 symbol 하나씩 확인
    for symbol in morse.get(key):
        # symbol이 '-'면 length에 3을 더하기
        if symbol == '-':
            length += 3
        # 아니면(= '.'이면) length에 1을 더하기
        else:
            length += 1
    # 모스 부호의 symbol이 n개라면 symbol 사이의 간격은 n-1 개
    length += (len(morse.get(key)) - 1) * 1
# 입력된 문장의 알파벳 개수가 n개라면 알파벳 사이의 간격은 n-1 개
length += (len(s) - 1) * 3

print(length)